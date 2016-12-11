#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    0:15
__author__ =    Xia Shuang Xi
Tornado 协程化
"""


import tornado.web
import tornado.httpclient
import tornado.gen
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        # 耗时操作，调用yield关键字获取异步对象的处理结果
        response = yield http.fetch('http://www.baidu.com')
        self.write(chunk=response.body)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
