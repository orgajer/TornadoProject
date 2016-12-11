#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    10:01
__author__ =    Xia Shuang Xi
"""


import tornado.web
import tornado.gen
import logging


def echo(message, callback):
    callback(message, 'that is callback message, In Echo Function!')


@tornado.gen.coroutine
def test():
    response = yield tornado.gen.Task(echo, 'this is first message')
    logging.warn(response.args[1])
    raise tornado.gen.Return('xxx')

test()

if __name__ == "__main__":
    pass