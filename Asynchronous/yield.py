#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 

def fun(max):
    n, a, b = 0, 0, 1
    while n<max:
        print b
        a, b = b, a + b
        n += 1

fun(8)

print "*" * 20

def fun2(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a + b
        n += 1

for i in fun2(8):
    print i