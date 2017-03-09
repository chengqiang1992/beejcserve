"""
应用程序配置
    class tornado.web.Application(handlers=None, default_host='', transforms=None, **settings)

    组成一个web应用程序的请求处理程序的集合。

    该类的实例是可调用的并且可以被直接传递给 HTTPServer 为应用程序提供服务：
        __________________________________________________
        application = tornado.web.Application([
            (r"/", MainPageHandler)
        ])
        http_server = http.server.HTTPServer(application)
        http_server.listen(8080)
        tornado.ioloop.IOLoop.current().start()
        -------------------------------------------------
    这个类的构造器带有一个列表包含 URLSpec 对象或(正则表达式，请求类)元祖。当我们接收到请求，我们按顺序迭代该列表并且实
    例化和请求路径相匹配的正则表达式所对应的第一个请求类。请求类可以被指定为一个类对象或一个（完全有资格的）名字。

    每个元祖可以包含另外的部分，只要符合 URLSpec 构造器参数的条件。（在 Tornado 3.2 之前，只允许包含两个或三个元素的元祖）

    一个字典可以作为该元素的第三个元素被传递，它将被用作用于处理程序构造器的关键字参数和 initialize 方法。这种模式也被用
    于例子中的 StaticFileHandler （注意一个 StaticFileHandler 可以被自动挂在连带下面的 static_path设置）：
        _______________________________________________________________________
            application = web.Application([
                (r"/static/(.*)", web.StaticFileHandler, {"path": "/var/www"}),
            ])
        -----------------------------------------------------------------------
    我们支持虚拟主机通过 add_handlers 方法，该方法带有一个主机正则表达式作为第一个参数：
        ____________________________________________________
            application.add_handlers(r"www\.myhost\.com", [
                (r"/article/([0-9]+)", ArticleHandler),
            ])
        ----------------------------------------------------
    你可以提供静态文件服务通过传递 static_path 配置作为关键字参数。我们将提供这些文件从 /static/ URI （这里可配置的通过
    static_url_prefix 配置），并且我们将提供 /favicon.ioc 和 /robots.txt 从相同目录下，一个 StaticFileHandler 的自定义子
    类可以被制定，通过static_handler_class设置。

    settings
        一般设置：
            autoreload
            debug
            default_handler_class
            compress_response
            gzip:
            log_function
            server_traceback
            ui_modules & ui_methods
            cookie_secret
            key_version
            login_url
            xsrf_cookies
            xsrf_cookie_version
            xsrf_cookir_kwargs
        模板设置
            autoescape
            xhtml_escape
            template_path
            template_loader
            template_whitespace
        静态路径设置
            static_hash_cache
            static_path
            static_url_prefix
            static_handler_class & static_handler_args

    listen(port, address='', **kwargs)
        为应用程序在给定端口上启动一个HTTP server

        这是一个方便的别名用来创建一个 HTTPServer 对象并调用它的listen方法。HTTPServer.listen不支持传递关键字参数给 HTTPServer
        构造器。对于高级用途（e.g. 多进程模式）不要使用这个方法。创建一个 HTTPServer 并直接调用它的 TCPServer.bind/TCPServer.start
        方法。

        注意在嗲用这个方法之后你仍然需要调用 IOLoop.current().start() 来启动该服务。

        返回 HTTPServer 对象

        在4.3版本更改：现在返回 HTTPServer 对象。

    add_handlers(host_pattern, host_handlers)
        添加給定的handler到我們的handlers表
    reverse_url(name, *args)
        返回名为 name 的handler的URL路径
        处理程序必须作为 URLSpec 添加到应用程序
        捕获组的参数将在 URLSpec 的正则表达式被替换。如有必要它们将转换成string
    log_request(handler)
        写一个完成的HTTP请求到日志中。

    class tornado.web.URLSpec(pattern, handler, kwargs=None, name=None)
        指定URL和处理程序之间的映射
        Parameters:
            pattern: 被匹配的正则表达式。任何正则表达式的group都将作为参数传递给程序 get/post 等方法。
            handler: 被调用的 RequsetHandler 子类
            kwargs(option): 将被传递给程序处理构造器的额外参数组成的字典
            name(optional): 该处理程序的名称，被 Application.reverse_url使用
"""



