"""
``tornado.web`` provides a simple web framework with asynchronous features that allow it to scale to large numbers of
open connections, making it ideal for `long polling`

Here is a simple "Hello, world" example app:

.. testcode::
    import tornado.ioloop
    import tornado.web


    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello World")


    if __name__ == "__main__":
        application = tornado.web.Application([
            (r"/", MainHandler),
        ])
        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()
.. testoutput::
    :hide:

See the :doc: `guide` for additional information.

Thread-safety notes
-------------------

In general, methods on `RequestHandler` and elsewhere in Tornado are not thread-safe.  In particular, methods such as
`~RequestHandler.write()`, `~RequestHandler.finish()`, and `~RequestHandler.flush()` must only be called from the main
thread. If you use multiple threads it is important to use `.IOLoop.add_callback` to transfer control back to the main
thread before finishing the request.
"""

from __future__ import absolute_import, division, print_function, with_statement

import base64
import binascii
import datetime
import email.utils
import functools
import gzip
import hashlib
import hmac
import mimetypes
import numbers
import os.path
import re
import stat
import sys
import threading
import time
import tornado
import traceback
import types
from io import BytesIO

from tornado.concurrent import Future
from tornado import escape
from tornado import gen
from tornado import httputil
from tornado import iostream
from tornado import locale
from tornado.log import access_log, app_log, gen_log
from tornado import stack_context
from tornado import template
from tornado.escape import utf8, _unicode
from tornado.util import (import_object, ObjectDict, raise_exc_info,
                          unicode_type, _websocket_mask)
from tornado.httputil import split_host_and_port

try:
    import Cookie   # py2
except ImportError:
    import http.cookies as Cookie       # py3

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


MIN_SUPPORTED_SIGNED_VALUE_VERSION = 1
"""
这个 Tornado 版本所支持的最旧的签名值版本。

比这个签名值更旧的版本将不能被解码。

.. versionadded::3.2.1
"""

MAX_SUPPORTED_SIGNED_VALUE_VERSION = 2
"""
这个 Tornado 版本所支持的最新的签名值版本。

比这个签名值更新的版本将不能被解码。

.. versionadded::3.2.1
"""

DEFAULT_SIGNED_VALUE_VERSION = 2
"""签名值版本通过 `.RequestHandler.create_signed_value` 产生.

可通过传递一个 ``version`` 关键字参数复写.

.. versionadded:: 3.2.1
"""

DEFAULT_SIGNED_VALUE_MIN_VERSION = 1
"""可以被 `.RequestHandler.get_secure_cookie` 接受的最旧的签名值.

可通过传递一个 ``min_version`` 关键字参数复写.

.. versionadded:: 3.2.1
"""

class RequestHandler(object):
    """
    HTTP 请求处理的基类。

    子类至少应该是以下"Entry points"部分中被定义的方法其中之一。
    """
    SUPPORTED_METHODS = ("GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")

    _template_loaders = {}      # {path: template.BaseLoader}
    _template_loaders_lock = threading.lock()
    _remove_control_chars_regex = re.compile(r"[\x00-\x08\x0e-\x1f]")

    def __init__(self, application, request, **kwargs):
        super(RequestHandler, self).__init__()

        self.application = application
        self.request = request
        self._headers_written = False
        self._finished = True
        self._auto_fish = True
        self._transforms = None
        self._prepared_future = None
        self.path_args = None
        self.path_kwargs = None
        self.ui = ObjectDict((n, self._ui_method(m)) for n, m in application.ui_methods.items())
        # UIModules are available as both `modules` and `_tt_modules` in the
        # template namespace.  Historically only `modules` was available
        # but could be clobbered by user additions to the namespace.
        # The template {% module %} directive looks in `_tt_modules` to avoid
        # possible conflicts.
        self.ui["_tt_modules"] = _UIModuleNamespace(self,
                                                    application.ui_modules)
        self.ui["modules"] = self.ui["_tt_modules"]
        self.clear()
        self.request.connection.set_close_callback(self.on_connection_close)
        self.initialize(**kwargs)

    def initialize(self):
        """
        子类初始化(Hook).

        作为url spec的第三个参数传递的字典，将作为关键字参数提供给initialize().

        例子::
            class ProfileHeadler(RequestHandler):
                def initialize(self, database):
                    self.database = database

                def get(self, username):
                    ...
            app = Application([
                (r'/user/(.*)', ProfileHandler, dict(database=database)),
                ])
        """
        pass

    @property
    def settings(self):
        """ `self.application.settings <Application.settings>` 的别名。"""
        return self.application.settings

    def head(self, *args, **kwargs):
        raise HTTPError(405)

    def get(self, *args, **kwargs):
        raise HTTPError(405)

    def post(self, *args, **kwargs):
        raise HTTPError(405)

    def delete(self, *args, **kwargs):
        raise HTTPError(405)

    def patch(self, *args, **kwargs):
        raise HTTPError(405)

    def put(self, *args, **kwargs):
        raise HTTPError(405)

    def options(self, *args, **kwargs):
        raise HTTPError(405)

    def prepare(self):
        """
        在每个请求的最开始被调用，在`get`/`post`/等方法之前

        通过复写这个方法，可以执行共同的初始化，而不用考虑每个请求的方法。

        异步支持：这个方法使用 `.gen.coroutine` 或 `.return_future`装饰器来使它异步（`asynchronous` 装饰器不能被用在
        `prepare`. 如果这个方法返回一个 `.Future` 对象, 执行将不再进行, 直到`.Future` 对象完成.）

        .. versionadded:: 3.1
           异步支持.
        """
        pass

    def on_finish(self):
        """
        在一个请求结束后被调用

        复写这个方法执行清理，日志记录等。这个方法和`prepare`是相对应的。``on_finish`` 可能不产生任何输出，因为它是在
        响应被送到客户端后才调用。
        """
        pass

    def on_connection_close(self):
        """
        在异步处理中，如果客户端关闭了链接将会被调用。

        复写这个方法来清楚与长连接的相关的资源。注意这个方法只有当在异步处理连接被关闭才会被调用；如果你需要在每个请求
        之后做清理，请复写`on_finish` 方法来代替.

        在客户端离开后，代理可能会保持连接一段时间（也可以是无限期），所以这个方法在终端用户关闭他们的连接时可能不会被
        立即执行。
        """
        if _has_stream_request_body(self.__class__):
            if not self.request.body.done():
                self.request.body.set_exception(iostream.StreamBufferFullError)
                self.request.body.exception()

    def clear(self):
        """重置这个响应的所有头部和内容。"""
        self._headers = httputil.HTTPHeaders({
            "Server": "TornadoServer/%s" % tornado.version,
            "Content-Type": "text/html; charset=UTF-8",
            "Date": httputil.format_timestamp(time.time()),
        })
        self.set_default_headers()
        self._write_buffer = []
        self._status_code = 200
        self._reason = httputil.responses[200]

    def set_default_headers(self):
        """复写这个方法可以在请求开始的时候设置HTTP头.

        例如, 在这里可以设置一个自定义 ``Server`` 头. 注意在一般的
        请求过程流里可能不会实现你预期的效果, 因为头部可能在错误处
        理(error handling)中被重置.
        """
        pass

    def set_status(self, status_code, reason=None):
        """设置响应的状态码.

        :arg int status_code: 响应状态码. 如果 ``reason`` 是 ``None``,
            它必须存在于 `httplib.responses <http.client.responses>`.
        :arg string reason: 用人类可读的原因短语来描述状态码.
            如果是 ``None``, 它会由来自
            `httplib.responses <http.client.responses>` 的reason填满.
        """
        self._status_code = status_code
        if reason is not None:
            self._reason = escape.native_str(reason)
        else:
            try:
                self._reason = httputil.responses[status_code]
            except KeyError:
                raise ValueError("unknown status code %d", status_code)

    def get_status(self):
        """返回响应的状态码."""
        return self._status_code

    def set_header(self, name, value):
        """给响应设置指定的头部和对应的值.

        如果给定了一个datetime, 我们会根据HTTP规范自动的对它格式化.
        如果值不是一个字符串, 我们会把它转换成字符串. 之后所有头部的值
        都将用UTF-8 编码.
        """
        self._headers[name] = self._convert_header_value(value)

        def add_header(self, name, value):
            """添加指定的响应头和对应的值.

            不像是 `set_header`, `add_header` 可以被多次调用来为相同的头
            返回多个值.
            """
            self._headers.add(name, self._convert_header_value(value))

    def clear_header(self, name):
        """清除输出头, 取消之前的 `set_header` 调用.

        注意这个方法不适用于被 `add_header` 设置了多个值的头.
        """
        if name in self._headers:
            del self._headers[name]

    _INVALID_HEADER_CHAR_RE = re.compile(br"[\x00-\\xlf]]")

    def _convert_header_value(self, value):
        if isinstance(value, bytes):
            pass
        elif isinstance(value, unicode_type):
            value = value.encode('utf-8')
        elif isinstance(value, numbers.Integral):
            # return immediately since we know the converted value will be safe
            return str(value)
        elif isinstance(value, datetime.datetime):
            return httputil.format_timestamp(value)
        else:
            raise TypeError("Unsupported header value %r" % value)
        # If \n is allowed into the header, it is possible to inject
        # additional headers or split the request.
        if RequestHandler._INVALID_HEADER_CHAR_RE.search(value):
            raise ValueError("Unsafe header value %r", value)
        return value

    _ARG_DEFAULT = []

    def get_argument(self, name, default=_ARG_DEFAULT, strip=True):
        """返回指定的name参数的值.

        如果没有提供默认值, 那么这个参数将被视为是必须的, 并且当
        找不到这个参数的时候我们会抛出一个 `MissingArgumentError`.

        如果一个参数在url上出现多次, 我们返回最后一个值.

        返回值永远是unicode.
        """
        return self._get_argument(name, default, self.request.arguments, strip)

    def get_arguments(self, name, strip=True):
        """返回指定name的参数列表.

        如果参数不存在, 返回一个空列表.

        返回值永远是unicode.
        """

        # Make sure `get_arguments` isn't accidentally being called with a
        # positional argument that's assumed to be a default (like in
        # `get_argument`.)
        assert isinstance(strip, bool)

        return self._get_arguments(name, self.request.arguments, strip)

    def get_body_argument(self, name, default=_ARG_DEFAULT, strip=True):
        """返回请求体中指定name的参数的值.

        如果没有提供默认值, 那么这个参数将被视为是必须的, 并且当
        找不到这个参数的时候我们会抛出一个 `MissingArgumentError`.

        如果一个参数在url上出现多次, 我们返回最后一个值.

        返回值永远是unicode.

        .. versionadded:: 3.2
        """
        return self._get_argument(name, default, self.request.body_arguments,
                                  strip)

    def get_body_arguments(self, name, strip=True):
        """返回由指定请求体中指定name的参数的列表.

        如果参数不存在, 返回一个空列表.

        返回值永远是unicode.

        .. versionadded:: 3.2
        """
        return self._get_arguments(name, self.request.body_arguments, strip)

    def get_query_argument(self, name, default=_ARG_DEFAULT, strip=True):
        """从请求的query string返回给定name的参数的值.

        如果没有提供默认值, 这个参数将被视为必须的, 并且当找不到这个
        参数的时候我们会抛出一个 `MissingArgumentError` 异常.

        如果这个参数在url中多次出现, 我们将返回最后一次的值.

        返回值永远是unicode.

        .. versionadded:: 3.2
        """
        return self._get_argument(name, default,
                                  self.request.query_arguments, strip)

    def get_query_arguments(self, name, strip=True):
        """返回指定name的参数列表.

        如果参数不存在, 将返回空列表.

        返回值永远是unicode.

        .. versionadded:: 3.2
        """
        return self._get_arguments(name, self.request.query_arguments, strip)

    def _get_argument(self, name, default, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            if default is self._ARG_DEFAULT:
                raise MissingArgumentError(name)
            return default
        return args[-1]

    def _get_arguments(self, name, source, strip=True):
        values = []
        for v in source.get(name, []):
            v = self.decode_argument(v, name=name)
            if isinstance(v, unicode_type):
                # Get rid of any weird control chars (unless decoding gave
                # us bytes, in which case leave it alone)
                v = RequestHandler._remove_control_chars_regex.sub(" ", v)
            if strip:
                v = v.strip()
            values.append(v)
        return values

    def decode_argument(self, value, name=None):
        """从请求中解码一个参数.

        这个参数已经被解码现在是一个字节字符串(byte string). 默认情况下,
        这个方法会把参数解码成utf-8并且返回一个unicode字符串, 但是它可以
        被子类复写.

        这个方法既可以在 `get_argument()` 中被用作过滤器, 也可以用来从url
        中提取值并传递给 `get()`/`post()`/等.

        如果知道的话参数的name会被提供, 但也可能为None
        (e.g. 在url正则表达式中未命名的组).
        """
        try:
            return _unicode(value)
        except UnicodeDecodeError:
            raise HTTPError(400, "Invalid unicode in %s: %r" %
                            (name or "url", value[:40]))

    @property
    def cookies(self):
        """ `self.request.cookies <.httputil.HTTPServerRequest.cookies>`
        的别名."""
        return self.request.cookies

    def get_cookie(self, name, default=None):
        """获取给定name的cookie值, 如果未获取到则返回默认值."""
        if self.request.cookies is not None and name in self.request.cookies:
            return self.request.cookies[name].value
        return default

    def set_cookie(self, name, value, domain=None, expires=None, path="/",
                   expires_days=None, **kwargs):
        """设置给定的cookie 名称/值还有其他给定的选项.

        另外的关键字参数在Cookie.Morsel直接设置.
        参见 https://docs.python.org/2/library/cookie.html#morsel-objects
        查看可用的属性.
        """
        # The cookie library only accepts type str, in both python 2 and 3
        name = escape.native_str(name)
        value = escape.native_str(value)
        if re.search(r"[\x00-\x20]", name + value):
            # Don't let us accidentally inject bad stuff
            raise ValueError("Invalid cookie %r: %r" % (name, value))
        if not hasattr(self, "_new_cookie"):
            self._new_cookie = Cookie.SimpleCookie()
        if name in self._new_cookie:
            del self._new_cookie[name]
        self._new_cookie[name] = value
        morsel = self._new_cookie[name]
        if domain:
            morsel["domain"] = domain
        if expires_days is not None and not expires:
            expires = datetime.datetime.utcnow() + datetime.timedelta(
                days=expires_days)
        if expires:
            morsel["expires"] = httputil.format_timestamp(expires)
        if path:
            morsel["path"] = path
        for k, v in kwargs.items():
            if k == 'max_age':
                k = 'max-age'

            # skip falsy values for httponly and secure flags because
            # SimpleCookie sets them regardless
            if k in ['httponly', 'secure'] and not v:
                continue

            morsel[k] = v

    def clear_cookie(self, name, path="/", domain=None):
        """删除给定名称的cookie.

        受cookie协议的限制, 必须传递和设置该名称cookie时候相同的path
        和domain来清除这个cookie(但是这里没有方法来找出在服务端所使
        用的该cookie的值).
        """
        expires = datetime.datetime.utcnow() - datetime.timedelta(days=365)
        self.set_cookie(name, value="", path=path, expires=expires,
                        domain=domain)

    def clear_all_cookies(self, path="/", domain=None):
        """删除用户在本次请求中所有携带的cookie.

        查看 `clear_cookie` 方法来获取关于path和domain参数的更多信息.

        .. versionchanged:: 3.2

           添加 ``path`` 和 ``domain`` 参数.
        """
        for name in self.request.cookies:
            self.clear_cookie(name, path=path, domain=domain)

    def set_secure_cookie(self, name, value, expires_days=30, version=None,
                          **kwargs):
        """给cookie签名和时间戳以防被伪造.

        你必须在你的Application设置中指定 ``cookie_secret`` 来使用这个方法.
        它应该是一个长的, 随机的字节序列作为HMAC密钥来做签名.

        使用 `get_secure_cookie()` 方法来阅读通过这个方法设置的cookie.

        注意 ``expires_days`` 参数设置cookie在浏览器中的有效期, 并且它是
        独立于 `get_secure_cookie` 的 ``max_age_days`` 参数的.

        安全cookie(Secure cookies)可以包含任意字节的值, 而不只是unicode
        字符串(不像是普通cookie)

        .. versionchanged:: 3.2.1

           添加 ``version`` 参数. 提出cookie version 2
           并将它作为默认设置.
        """
        self.set_cookie(name, self.create_signed_value(name, value,
                                                       version=version),
                        expires_days=expires_days, **kwargs)

    def create_signed_value(self, name, value, version=None):
        """产生用时间戳签名的字符串, 防止被伪造.

        一般通过set_secure_cookie 使用, 但对于无cookie使用来说就
        作为独立的方法来提供. 为了解码不作为cookie存储的值, 可以
        在 get_secure_cookie 使用可选的value参数.

        .. versionchanged:: 3.2.1

           添加 ``version`` 参数. 提出cookie version 2
           并将它作为默认设置.
        """
        self.require_setting("cookie_secret", "secure cookies")
        secret = self.application.settings["cookie_secret"]
        key_version = None
        if isinstance(secret, dict):
            if self.application.settings.get("key_version") is None:
                raise Exception("key_version setting must be used for secret_key dicts")
            key_version = self.application.settings["key_version"]

        return create_signed_value(secret, name, value, version=version,
                                   key_version=key_version)

    def get_secure_cookie(self, name, value=None, max_age_days=31,
                          min_version=None):
        """如果给定的签名过的cookie是有效的,则返回，否则返回None.

        解码后的cookie值作为字节字符串返回(不像 `get_cookie` ).

        .. versionchanged:: 3.2.1

           添加 ``min_version`` 参数. 引进cookie version 2;
           默认版本 1 和 2 都可以接受.
        """
        self.require_setting("cookie_secret", "secure cookies")
        if value is None:
            value = self.get_cookie(name)
        return decode_signed_value(self.application.settings["cookie_secret"],
                                   name, value, max_age_days=max_age_days,
                                   min_version=min_version)

    def get_secure_cookie_key_version(self, name, value=None):
        """返回安全cookie(secure cookie)的签名key版本.

        返回的版本号是int型的.
        """
        self.require_setting("cookie_secret", "secure cookies")
        if value is None:
            value = self.get_cookie(name)
        return get_signature_key_version(value)

    def redirect(self, url, permanent=False, status=None):
        """重定向到给定的URL(可以选择相对路径).

        如果指定了 ``status`` 参数, 这个值将作为HTTP状态码; 否则
        将通过 ``permanent`` 参数选择301 (永久) 或者 302 (临时).
        默认是 302 (临时重定向).
        """
        if self._headers_written:
            raise Exception("Cannot redirect after headers have been written")
        if status is None:
            status = 301 if permanent else 302
        else:
            assert isinstance(status, int) and 300 <= status <= 399
        self.set_status(status)
        self.set_header("Location", utf8(url))
        self.finish()

    def write(self, chunk):
        """把给定块写到输出buffer.

        为了把输出写到网络, 使用下面的flush()方法.

        如果给定的块是一个字典, 我们会把它作为JSON来写同时会把响应头
        设置为 ``application/json``. (如果你写JSON但是设置不同的
        ``Content-Type``,  可以调用set_header *在调用write()之后* ).

        注意列表不能转换为JSON 因为一个潜在的跨域安全漏洞. 所有的JSON
        输出应该包在一个字典中. 更多细节参考
        http://haacked.com/archive/2009/06/25/json-hijacking.aspx/ 和
        https://github.com/facebook/tornado/issues/1009
        """
        if self._finished:
            raise RuntimeError("Cannot write() after finish()")
        if not isinstance(chunk, (bytes, unicode_type, dict)):
            message = "write() only accepts bytes, unicode, and dict objects"
            if isinstance(chunk, list):
                message += ". Lists not accepted for security reasons; see http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.write"
            raise TypeError(message)
        if isinstance(chunk, dict):
            chunk = escape.json_encode(chunk)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)

    def render(self, template_name, **kwargs):
        """使用给定参数渲染模板并作为响应."""
        html = self.render_string(template_name, **kwargs)

        # Insert the additional JS and CSS added by the modules on the page
        js_embed = []
        js_files = []
        css_embed = []
        css_files = []
        html_heads = []
        html_bodies = []
        for module in getattr(self, "_active_modules", {}).values():
            embed_part = module.embedded_javascript()
            if embed_part:
                js_embed.append(utf8(embed_part))
            file_part = module.javascript_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    js_files.append(file_part)
                else:
                    js_files.extend(file_part)
            embed_part = module.embedded_css()
            if embed_part:
                css_embed.append(utf8(embed_part))
            file_part = module.css_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    css_files.append(file_part)
                else:
                    css_files.extend(file_part)
            head_part = module.html_head()
            if head_part:
                html_heads.append(utf8(head_part))
            body_part = module.html_body()
            if body_part:
                html_bodies.append(utf8(body_part))

        def is_absolute(path):
            return any(path.startswith(x) for x in ["/", "http:", "https:"])

        if js_files:
            # Maintain order of JavaScript files given by modules
            paths = []
            unique_paths = set()
            for path in js_files:
                if not is_absolute(path):
                    path = self.static_url(path)
                if path not in unique_paths:
                    paths.append(path)
                    unique_paths.add(path)
            js = ''.join('<script src="' + escape.xhtml_escape(p) +
                         '" type="text/javascript"></script>'
                         for p in paths)
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + utf8(js) + b'\n' + html[sloc:]
        if js_embed:
            js = b'<script type="text/javascript">\n//<![CDATA[\n' + \
                 b'\n'.join(js_embed) + b'\n//]]>\n</script>'
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + js + b'\n' + html[sloc:]
        if css_files:
            paths = []
            unique_paths = set()
            for path in css_files:
                if not is_absolute(path):
                    path = self.static_url(path)
                if path not in unique_paths:
                    paths.append(path)
                    unique_paths.add(path)
            css = ''.join('<link href="' + escape.xhtml_escape(p) + '" '
                                                                    'type="text/css" rel="stylesheet"/>'
                          for p in paths)
            hloc = html.index(b'</head>')
            html = html[:hloc] + utf8(css) + b'\n' + html[hloc:]
        if css_embed:
            css = b'<style type="text/css">\n' + b'\n'.join(css_embed) + \
                  b'\n</style>'
            hloc = html.index(b'</head>')
            html = html[:hloc] + css + b'\n' + html[hloc:]
        if html_heads:
            hloc = html.index(b'</head>')
            html = html[:hloc] + b''.join(html_heads) + b'\n' + html[hloc:]
        if html_bodies:
            hloc = html.index(b'</body>')
            html = html[:hloc] + b''.join(html_bodies) + b'\n' + html[hloc:]
        self.finish(html)

    def render_string(self, template_name, **kwargs):
        """使用给定的参数生成指定模板.

        我们返回生成的字节字符串(以utf8). 为了生成并写一个模板
        作为响应, 使用上面的render().
        """
        # If no template_path is specified, use the path of the calling file
        template_path = self.get_template_path()
        if not template_path:
            frame = sys._getframe(0)
            web_file = frame.f_code.co_filename
            while frame.f_code.co_filename == web_file:
                frame = frame.f_back
            template_path = os.path.dirname(frame.f_code.co_filename)
        with RequestHandler._template_loader_lock:
            if template_path not in RequestHandler._template_loaders:
                loader = self.create_template_loader(template_path)
                RequestHandler._template_loaders[template_path] = loader
            else:
                loader = RequestHandler._template_loaders[template_path]
        t = loader.load(template_name)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.generate(**namespace)

    def get_template_namespace(self):
        """返回一个字典被用做默认的模板命名空间.

        可以被子类复写来添加或修改值.

        这个方法的结果将与 `tornado.template` 模块中其他的默认值
        还有 `render` 或 `render_string` 的关键字参数相结合.
        """
        namespace = dict(
            handler=self,
            request=self.request,
            current_user=self.current_user,
            locale=self.locale,
            _=self.locale.translate,
            pgettext=self.locale.pgettext,
            static_url=self.static_url,
            xsrf_form_html=self.xsrf_form_html,
            reverse_url=self.reverse_url
        )
        namespace.update(self.ui)
        return namespace

    def create_template_loader(self, template_path):
        """返回给定路径的新模板装载器.

        可以被子类复写. 默认返回一个在给定路径上基于目录的装载器,
        使用应用程序的 ``autoescape`` 和 ``template_whitespace``
        设置. 如果应用设置中提供了一个 ``template_loader`` ,
        则使用它来替代.
        """
        settings = self.application.settings
        if "template_loader" in settings:
            return settings["template_loader"]
        kwargs = {}
        if "autoescape" in settings:
            # autoescape=None means "no escaping", so we have to be sure
            # to only pass this kwarg if the user asked for it.
            kwargs["autoescape"] = settings["autoescape"]
        if "template_whitespace" in settings:
            kwargs["whitespace"] = settings["template_whitespace"]
        return template.Loader(template_path, **kwargs)

    def flush(self, include_footers=False, callback=None):
        """将当前输出缓冲区写到网络.

        ``callback`` 参数, 如果给定则可用于流控制: 它会在所有数据被写到
        socket后执行. 注意同一时间只能有一个flush callback停留; 如果另
        一个flush在前一个flush的callback运行之前发生, 那么前一个callback
        将会被丢弃.

        .. versionchanged:: 4.0
           现在如果没有给定callback, 会返回一个 `.Future` 对象.
        """
        chunk = b"".join(self._write_buffer)
        self._write_buffer = []
        if not self._headers_written:
            self._headers_written = True
            for transform in self._transforms:
                self._status_code, self._headers, chunk = \
                    transform.transform_first_chunk(
                        self._status_code, self._headers,
                        chunk, include_footers)
            # Ignore the chunk and only write the headers for HEAD requests
            if self.request.method == "HEAD":
                chunk = None

            # Finalize the cookie headers (which have been stored in a side
            # object so an outgoing cookie could be overwritten before it
            # is sent).
            if hasattr(self, "_new_cookie"):
                for cookie in self._new_cookie.values():
                    self.add_header("Set-Cookie", cookie.OutputString(None))

            start_line = httputil.ResponseStartLine('',
                                                    self._status_code,
                                                    self._reason)
            return self.request.connection.write_headers(
                start_line, self._headers, chunk, callback=callback)
        else:
            for transform in self._transforms:
                chunk = transform.transform_chunk(chunk, include_footers)
            # Ignore the chunk and only write the headers for HEAD requests
            if self.request.method != "HEAD":
                return self.request.connection.write(chunk, callback=callback)
            else:
                future = Future()
                future.set_result(None)
                return future

    def write_error(self, status_code, **kwargs):
        """复写这个方法来实现自定义错误页.

        ``write_error`` 可能调用 `write`, `render`, `set_header`,等
        来产生一般的输出.

        如果错误是由未捕获的异常造成的(包括HTTPError), 三个一组的
        ``exc_info`` 将变成可用的通过 ``kwargs["exc_info"]``.
        注意这个异常可能不是"当前(current)" 目的或方法的异常就像
        ``sys.exc_info()`` 或 ``traceback.format_exc``.
        """
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header('Content-Type', 'text/plain')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        else:
            self.finish("<html><title>%(code)d: %(message)s</title>"
                        "<body>%(code)d: %(message)s</body></html>" % {
                            "code": status_code,
                            "message": self._reason,
                        })

    @property
    def locale(self):
        """返回当前session的位置.

        通过 `get_user_locale` 来确定, 你可以复写这个方法设置
        获取locale的条件, e.g., 记录在数据库中的用户偏好, 或
        `get_browser_locale`, 使用 ``Accept-Language`` 头部.

        .. versionchanged: 4.1
           添加setter属性.
        """
        if not hasattr(self, "_locale"):
            self._locale = self.get_user_locale()
            if not self._locale:
                self._locale = self.get_browser_locale()
                assert self._locale
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    def get_user_locale(self):
        """复写这个方法确定认证过的用户所在位置.

        如果返回了None , 我们退回选择 `get_browser_locale()`.

        这个方法应该返回一个 `tornado.locale.Locale` 对象,
        就像调用 ``tornado.locale.get("en")`` 得到的那样
        """
        return None

    def get_browser_locale(self, default="en_US"):
        """从 ``Accept-Language`` 头决定用户的位置.

        参考 http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4
        """
        if "Accept-Language" in self.request.headers:
            languages = self.request.headers["Accept-Language"].split(",")
            locales = []
            for language in languages:
                parts = language.strip().split(";")
                if len(parts) > 1 and parts[1].startswith("q="):
                    try:
                        score = float(parts[1][2:])
                    except (ValueError, TypeError):
                        score = 0.0
                else:
                    score = 1.0
                locales.append((parts[0], score))
            if locales:
                locales.sort(key=lambda pair: pair[1], reverse=True)
                codes = [l[0] for l in locales]
                return locale.get(*codes)
        return locale.get(default)

    @property
    def current_user(self):
        """返回请求中被认证的用户.

        可以使用以下两者之一的方式来设置:

        * 子类可以复写 `get_current_user()`, 这将会在第一次访问
          ``self.current_user`` 时自动被调用.
          `get_current_user()` 在每次请求时只会被调用一次, 并为
          将来访问做缓存::

              def get_current_user(self):
                  user_cookie = self.get_secure_cookie("user")
                  if user_cookie:
                      return json.loads(user_cookie)
                  return None

        * 它可以被设置为一个普通的变量, 通常在来自被复写的 `prepare()`::

              @gen.coroutine
              def prepare(self):
                  user_id_cookie = self.get_secure_cookie("user_id")
                  if user_id_cookie:
                      self.current_user = yield load_user(user_id_cookie)

        注意 `prepare()` 可能是一个协程, 尽管 `get_current_user()`
        可能不是, 所以如果加载用户需要异步操作后面的形式是必要的.

        用户对象可以是application选择的任意类型.
        """
        if not hasattr(self, "_current_user"):
            self._current_user = self.get_current_user()
        return self._current_user

    @current_user.setter
    def current_user(self, value):
        self._current_user = value

    def get_current_user(self):
        """复写来实现获取当前用户, e.g., 从cookie得到.

        这个方法可能不是一个协程.
        """
        return None

    def get_login_url(self):
        """复写这个方法自定义基于请求的登陆URL.

        默认情况下, 我们使用application设置中的 ``login_url`` 值.
        """
        self.require_setting("login_url", "@tornado.web.authenticated")
        return self.application.settings["login_url"]

    def get_template_path(self):
        """可以复写为每个handler指定自定义模板路径.

        默认情况下, 我们使用应用设置中的 ``template_path`` .
        如果返回None则使用调用文件的相对路径加载模板.
        """
        return self.application.settings.get("template_path")

    @property
    def xsrf_token(self):
        """当前用户/会话的XSRF-prevention token.

        为了防止伪造跨站请求, 我们设置一个 '_xsrf' cookie 并在所有POST
        请求中包含相同的 '_xsrf' 值作为一个参数. 如果这两个不匹配,
        我们会把这个提交当作潜在的伪造请求而拒绝掉.

        查看 http://en.wikipedia.org/wiki/Cross-site_request_forgery

        .. versionchanged:: 3.2.2
           该xsrf token现在已经在每个请求都有一个随机mask这使得它
           可以简洁的把token包含在页面中是安全的. 查看
           http://breachattack.com 浏览更多信息关于这个更改修复的
           问题. 旧(版本1)cookies 将被转换到版本2 当这个方法被调用
           除非 ``xsrf_cookie_version`` `Application` 被设置为1.

        .. versionchanged:: 4.3
           该 ``xsrf_cookie_kwargs`` `Application` 设置可能被用来
           补充额外的cookie 选项(将会直接传递给 `set_cookie`).
           例如, ``xsrf_cookie_kwargs=dict(httponly=True, secure=True)``
           将设置 ``secure`` 和 ``httponly`` 标志在 ``_xsrf`` cookie.
        """
        if not hasattr(self, "_xsrf_token"):
            version, token, timestamp = self._get_raw_xsrf_token()
            output_version = self.settings.get("xsrf_cookie_version", 2)
            cookie_kwargs = self.settings.get("xsrf_cookie_kwargs", {})
            if output_version == 1:
                self._xsrf_token = binascii.b2a_hex(token)
            elif output_version == 2:
                mask = os.urandom(4)
                self._xsrf_token = b"|".join([
                    b"2",
                    binascii.b2a_hex(mask),
                    binascii.b2a_hex(_websocket_mask(mask, token)),
                    utf8(str(int(timestamp)))])
            else:
                raise ValueError("unknown xsrf cookie version %d",
                                 output_version)
            if version is None:
                expires_days = 30 if self.current_user else None
                self.set_cookie("_xsrf", self._xsrf_token,
                                expires_days=expires_days,
                                **cookie_kwargs)
        return self._xsrf_token

    def _get_raw_xsrf_token(self):
        """读取或生成xsrf token 用它原本的格式.

        该raw_xsrf_token是一个tuple 包含:

        * version: 读到这个token的cookie的版本,或None如果我们在该请求
          中生成一个新token.
        * token: 原生的token数据; 随机(non-ascii) bytes.
        * timestamp: 该token生成的时间(对于版本1的cookie将不准确)
        """
        if not hasattr(self, '_raw_xsrf_token'):
            cookie = self.get_cookie("_xsrf")
            if cookie:
                version, token, timestamp = self._decode_xsrf_token(cookie)
            else:
                version, token, timestamp = None, None, None
            if token is None:
                version = None
                token = os.urandom(16)
                timestamp = time.time()
            self._raw_xsrf_token = (version, token, timestamp)
        return self._raw_xsrf_token

    def _decode_xsrf_token(self, cookie):
        """把_get_raw_xsrf_token返回的cookie字符串转换成元组形式.
        """

        try:
            m = _signed_value_version_re.match(utf8(cookie))

            if m:
                version = int(m.group(1))
                if version == 2:
                    _, mask, masked_token, timestamp = cookie.split("|")

                    mask = binascii.a2b_hex(utf8(mask))
                    token = _websocket_mask(
                        mask, binascii.a2b_hex(utf8(masked_token)))
                    timestamp = int(timestamp)
                    return version, token, timestamp
                else:
                    # Treat unknown versions as not present instead of failing.
                    raise Exception("Unknown xsrf cookie version")
            else:
                version = 1
                try:
                    token = binascii.a2b_hex(utf8(cookie))
                except (binascii.Error, TypeError):
                    token = utf8(cookie)
                # We don't have a usable timestamp in older versions.
                timestamp = int(time.time())
                return (version, token, timestamp)
        except Exception:
            # Catch exceptions and return nothing instead of failing.
            gen_log.debug("Uncaught exception in _decode_xsrf_token",
                          exc_info=True)
            return None, None, None

    def static_url(self, path, include_host=None, **kwargs):
        """为给定的相对路径的静态文件返回一个静态URL.

        这个方法需要你在你的应用中设置 ``static_path`` (既你
        静态文件的根目录).

        这个方法返回一个带有版本的url (默认情况下会添加
        ``?v=<signature>``), 这会允许静态文件被无限期缓存. 这可以被
        禁用通过传递 ``include_version=False`` (默认已经实现;
        其他静态文件的实现不需要支持这一点, 但它们可能支持其他选项).

        默认情况下这个方法返回当前host的相对URL, 但是如果
        ``include_host`` 为true则返回的将是绝对路径的URL.
        如果这个处理函数有一个 ``include_host`` 属性, 该值将被所有的
        `static_url` 调用默认使用, 而不需要传递 ``include_host``
        作为一个关键字参数.

        """
        self.require_setting("static_path", "static_url")
        get_url = self.settings.get("static_handler_class",
                                    StaticFileHandler).make_static_url

        if include_host is None:
            include_host = getattr(self, "include_host", False)

        if include_host:
            base = self.request.protocol + "://" + self.request.host
        else:
            base = ""

        return base + get_url(self.settings, path, **kwargs)

    def listen(self, port, address="", **kwargs):
        """为应用程序在给定端口上启动一个HTTP server.

        这是一个方便的别名用来创建一个 `.HTTPServer` 对象并调用它
        的listen方法. `HTTPServer.listen <.TCPServer.listen>`
        不支持传递关键字参数给 `.HTTPServer` 构造器. 对于高级用途
        (e.g. 多进程模式), 不要使用这个方法; 创建一个
        `.HTTPServer` 并直接调用它的
        `.TCPServer.bind`/`.TCPServer.start` 方法.

        注意在调用这个方法之后你仍然需要调用
        ``IOLoop.current().start()`` 来启动该服务.

        返回 `.HTTPServer` 对象.

        .. versionchanged:: 4.3
           现在返回 `.HTTPServer` 对象.
        """
        # import is here rather than top level because HTTPServer
        # is not importable on appengine
        from tornado.httpserver import HTTPServer
        server = HTTPServer(self, **kwargs)
        server.listen(port, address)
        return server
