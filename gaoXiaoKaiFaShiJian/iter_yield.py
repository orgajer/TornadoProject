#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:43
__author__ =    Xia Shuang Xi
迭代器与yield
迭代器: 访问集合内元素的一种方式，迭代器不能回退，只能往前迭代
yield: 使用yield关键字的函数迭代器
"""

# list
print range(5)

# 迭代器
useIter = iter(range(5))
print useIter
print useIter.next()
print useIter.next()
print useIter.next()
print useIter.next()
print useIter.next()
# StopIteration
try:
    print useIter.next()
except Exception, e:
    print Exception, ":", e


# 生成器
def demo_iterator():
    print "I'm in the first call of next()"
    yield 1
    print "I'm in the second call of next()"
    yield 2
    print "I'm in the third call of next()"
    yield 3

for i in demo_iterator():
    print i
