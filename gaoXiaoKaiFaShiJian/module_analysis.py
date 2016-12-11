#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    10:23
__author__ =    Xia Shuang Xi
"""


import tornado.ioloop
import tornado.web
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    # 注册我们自己的回调函数，在读取完数据后，系统会根据url的匹配调用合适的RequestHandler
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler), ])

    # 创建HTTPServer，将Application好好的保护起来。
    http_server = tornado.httpserver.HTTPServer(app)

    # 此时默认会将读取网卡的所有ip进行绑定，当然你可以指定要绑定的ip。
    http_server.bind(11111)

    # 此时创建子进程，每个子进程会创建epoll，并且将绑定ip放入到epoll中，监听连接事件。
    http_server.start(3)

    # 开始死循环处理事件，先处理系统生成超时事件，而后处理网络事件。
    IOLoop.instance().start()