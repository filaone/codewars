#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys

string_1 = "中国中国中国中国中国中国中国"
print sys.getsizeof(string_1)

def take_nbytes(s, n):
    buf = ""  # buf has its own size
    print "enter : ---"
    for chara in list(s):
        if (sys.getsizeof(buf) + sys.getsizeof(chara) - 2*sys.getsizeof("") > n):
            return buf
        else:
            buf += chara
    return buf

print "\"\" has its own size 37, buf -37 and chara-37 should small than n"
print take_nbytes(string_1,10)
print take_nbytes(string_1,20)
print take_nbytes(string_1,37)
print take_nbytes(string_1,59)
print take_nbytes(string_1,70)
