#!/usr/bin/env python
# coding: utf8

"""
project: TornadoProject
create date: 2016/12/5
__author__ = xiashuangxi
tornado 异步请求示例
"""
from time import sleep
from tornado.httpclient import AsyncHTTPClient


def handle_response(response):
    # 并未运行到此处，整个程序就完成了
    print 'start handle...'
    print response.body
    print 'end handle...'


def asynchronous_visit():
    url = 'http://www.2cto.com/kf/201202/118133.html'
    http_client = AsyncHTTPClient()
    http_client.fetch(request=url, callback=handle_response)


if __name__ == "__main__":
    asynchronous_visit()
    print 'exit'
