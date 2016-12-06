#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import urllib
import json

from tornado.options import define, options
define("port", default=9000, help="run on the given port", type=int)

class IndexHandlerSync(tornado.web.RequestHandler):
    def get(self):
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://localhost/haoServer/index.php")
        body = json.loads(response.body)
        self.write(body)
        self.finish()

class IndexHandlerAsync(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://localhost/haoServer/index.php",
                                      callback=self.deal)
    
    def deal(self, response):
        body = json.loads(response.body)
        self.write(body)
        self.finish()

class IndexHandlerCoroutine(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://localhost/haoServer/index.php")
        body = json.loads(response.body)
        self.write(body)
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/sync", IndexHandlerSync),
        (r"/async", IndexHandlerAsync),
        (r"/coroutine", IndexHandlerCoroutine),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
