"""
tornado.web - RequestHandler 和 Application 类

    tornado.web 提供一种带有异步功能并允许它扩展到大量开发连接的简单的web框架，使其成为处理长连接(long pooling)的一种理
    想选择。

    这是是一个简单的“Hello， world”示例应用：
        _____________________________________________________
            import tornado.ioloop
            import tornado.web
            class MainHandler(tornado.web.RequestHandler):
                def get(self):
                    self.write("Hello, world")
            if __name__ == "__main__":
                application = tornado.web.Application([
                    (r"/", MainHandler)
                ])
                application.listen(8888)
                tornado.ioloop.IOLoop.current().start()
        ----------------------------------------------------
    通常一个 Tornado.web 应用包括一个或者多个 RequestHandler 子类，一个可以将收到的请求路由到对应 handler 的 Application
    对象和一个启动服务器的 main() 函数。

    Application 对象
        Application 对象和负责全局配置的，包括映射请求转发给处理程序的路由表。

        路由表是 URLSpec 对象(或元祖)的列表，其中每个都包含(至少)一个正则表达和一个处理类。顺序问题，第一个匹配的规则会
        被使用，如果正则表达包含捕获组，这些组会被作为路径参数传递给处理函数的HTTP方法。如果一个字典作为 URLSpec 的第三个
        参数被传递，它会作为初始参数传递给 RequestHandler.initialize。最后 URLSpec 可能有一个名字，这将允许他被 RequestHandler
        .reverse_url使用。

        例如，在这个片段中根 URL / 映射到了 MainHandler，像 /story/ 后跟着一个数组这种形式的 URL 被映射到了 StoryHandler
        , 这个数字被传递（作为字符串）给 StoryHandler.get。

    RequestHandler 子类
        Tornado web 应用程序的大部分工作是在 RequestHandler 子类下完成的。处理子类的主入口是一个命名为处理 HTTP 方法的函数：
        get(), post()等等。每个处理程序可以定义一个或者多个这种方法来处理不同的 HTTP 动作，如上所述，这些方法将被匹配路由
        规则的捕获组对应的参数调用。

        在处理程序中，调用方法如 RequestHandler.render 或者 RequestHandler.write 产生一个响应。 render() 通过名字加载一个
        Template并使用给定的参数渲染它。 write() 被用于非模板基础的输出，它接受字符串、字节和字典(字典会被编码成JSON)

        在 RequestHandler 中的很多方法的设计是为了在子类中复写和整个应用中使用，常用的方法是定义个 BaseHandler 类，复写
        一些方法例如 write_error 和 get_current_user 然后子类继承使用你自己的 BaseHandler 而不是 RequestHandler 在你所具
        体的处理程序中。

    线程安全说明
        一般情况下，在 RequestHandler 中的方法和 Tornado 中其他的方法不是线程安全的，尤其是一些方法，例如 write(), finish()
        和 flush() 要求只能从主线程调用。如果你使用多线程，那么在结束请求之前，使用 IOLoop.add_callback 来把控制权传送回
        主线成是很重要的。

        Request handlers
            HTTP 请求处理的基类
            子类至少应该是一下 "Entry points"部分中被定义的方法其中之一。
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('<a href="%s">link to story 1</a>' % self.reverse_url("story", "1"))
#
#
# class StoryHandler(tornado.web.RequestHandler):
#     def initialize(self, db):
#         self.db = db
#
#     def get(self, story_id):
#         self.write("this is story %s" % story_id)
#
# if __name__ == "__main__":
#     app = tornado.web.Application([
#         url(r"/", MainHandler),
#         url(r"/story/([0-9]+)", StoryHandler, dict(db=db), name="story")
#     ])