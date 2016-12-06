#!/usr/bin/env python
#coding: utf8

"""
project: TornadoProject
create date: 2016/12/5 
__author__ = xiashuangxi
tornado 同步请求示例
"""

from tornado.httpclient import HTTPClient   # tornado的HTTP客户端类


def synchronous_visit():
    http_client = HTTPClient()
    # 阻塞，直到对http://www.baidu.com访问完成
    response = http_client.fetch("http://www.baidu.com")
    print response.body

if __name__ == "__main__":
    synchronous_visit()
