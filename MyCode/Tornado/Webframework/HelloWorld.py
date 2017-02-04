"""
tornado.web  -- RequestHandler 和 Application 类
    tornado.web 提供了一种带有异步功能并允许它扩展到大量开放连接的简单的web框架，使其成为处理长连接 (long polling) 的
    一种理想选择
"""

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
