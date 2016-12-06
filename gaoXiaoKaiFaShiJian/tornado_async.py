#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:30
__author__ =    Xia Shuang Xi
Tornado异步化
"""

import tornado.web
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://www.baidu.com', callback=self.on_response)

    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)

        print response.body
        self.write(response.body)
        self.finish()


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
