#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    22:23
__author__ =    Xia Shuang Xi
在协程中等待多个异步调用
未运行成功
"""


# 引入协程库gen
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

@gen.coroutine
def coroutine_visit_list():
    http_client = AsyncHTTPClient()
    list_response = yield [
        http_client.fetch('www.baidu.com'),
        http_client.fetch('www.sina.com'),
        http_client.fetch('www.163.com'),
        http_client.fetch('www.google.com')
    ]

    for response in list_response:
        print response.body


@gen.coroutine
def coroutine_visit_dict():
    http_client = AsyncHTTPClient()
    dict_response = yield {
        "baidu": http_client.fetch('www.baidu.com'),
        "sina": http_client.fetch('www.sina.com'),
        "163": http_client.fetch('www.163.com'),
        "google": http_client.fetch('www.google.com')
    }

    print dict_response('sina').body

if __name__ == "__main__":
    coroutine_visit_list()

    coroutine_visit_dict()
