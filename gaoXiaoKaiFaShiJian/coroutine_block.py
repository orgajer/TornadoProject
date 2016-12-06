#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    0:15
__author__ =    Xia Shuang Xi
在协程中调用阻塞函数，有疑问
未运行成功
"""

import time
from tornado import gen
from concurrent.futures import ThreadPoolExecutor

thread_pool = ThreadPoolExecutor(2)


def my_sleep(count):
    for i in range(count):
        time.sleep(1)


@gen.coroutine
def call_blocking():
    print "start of call_blocking"
    yield thread_pool.submit(my_sleep, 10)
    # 后面的为什么不执行？
    print "end of call_blocking"


if __name__ == "__main__":
    print time.ctime()
    call_blocking()
    print time.ctime()
