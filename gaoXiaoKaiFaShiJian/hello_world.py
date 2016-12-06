#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    0:15
__author__ =    Xia Shuang Xi
Tornado Hello World 脚本
"""


import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')


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
