#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:58
__author__ =    Xia Shuang Xi
编写协程函数,为什么会失败?
未运行成功
"""

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch('http://www.baidu.com')
    print response.body


@gen.coroutine
def outer_coroutine():
    print "start call another coroutine"
    yield coroutine_visit()
    print "end of outer_coroutine"


def use_run_sync():
    print "start to call a coroutine"
    IOLoop().current().run_sync(lambda: coroutine_visit)
    print "end of calling a coroutine"

def use_spawn_callback():
    print "start to call a coroutine"
    IOLoop().current().spawn_callback(lambda: coroutine_visit)
    print "end of calling a coroutine"

if __name__ == "__main__":
    t = use_run_sync()
    print t
