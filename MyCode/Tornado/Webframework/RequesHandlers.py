# !/usr/bin/env python
"""
    Tornado.web 提供一种带有异步功能并允许它扩展到大量开发连接的简单的web框架，使其成为处理长连接(long pooling)的一种理
    想选择。

    线程安全说明
    -----------------
    一般情况下，在 RequestHandler 中的方法和 Tornado 中其他的方法不是线程安全的，尤其是一些方法，例如 write(), finish()
    和 flush() 要求只能从主线程调用。如果你使用多线程，那么在结束请求之前，使用 IOLoop.add_callback 来把控制权传送回
    主线成是很重要的。
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
from tornado import httpclient
from tornado import iostream
from tornado import locale
from  tornado.log import access_log, app_log, gen_log
from tornado import stack_context
from tornado import template
from tornado.escape import utf8, _unicode
from tornado.util import (import_object, ObjectDict, raise_exc_info, unicode_type, _websocket_mask)
from tornado.httputil import split_host_and_port

try:
    import Cookie # py2
except ImportError:
    import http.cookies as Cookie # py3

try:
    import urlparse # py2
except ImportError:
    import urllib.parse as urlparse #py3

try:
    from urllib import urlencode  # py2
except ImportError:
    from urllib.parse import urlencode  # py3

MIN_SUPPORTED_SIGNED_VALUE_VERSION = 1
"""这个Tornado版本所支持的最旧的签名值版本.

比这个签名值更旧的版本将不能被解码.

.. versionadded:: 3.2.1
"""

MAX_SUPPORTED_SIGNED_VALUE_VERSION = 2
"""这个Tornado版本所支持的最新的签名值版本.

比这个签名值更新的版本将不能被解码.

.. versionadded:: 3.2.1
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
        子类至少应该是一下"Entry points"部分中被定义的方法其中之一。
        SUPPORTED_METHODS = ("GET", "HEAD", "POST", "DELETE", "PATCH", "PUT",
                         "OPTIONS")

        _template_loaders = {}  # {path: template.BaseLoader}
        _template_loader_lock = threading.Lock()
        _remove_control_chars_regex = re.compile(r"[\x00-\x08\x0e-\x1f]")

        def __init__(self, application, request, **kwargs):
            super(RequestHandler, self).__init__()

            self.application = application
            self.request = request
            self._headers_written = False
            self._finished = False
            self._auto_finish = True
            self._transforms = None  # will be set in _execute
            self._prepared_future = None
            self.path_args = None
            self.path_kwargs = None
            self.ui = ObjectDict((n, self._ui_method(m)) for n, m in
                                 application.ui_methods.items())
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




