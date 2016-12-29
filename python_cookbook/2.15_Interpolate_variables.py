#!/usr/bin/python
#-*- coding:utf-8 -*-

# 2.15 Interpolating Variables In Strings

print(vars())
s = '{name} has {n} messages'
print(s.format(name='wangshuguang', n=1000))
name = 'wangshuguang'
n = 1000000
fm = s.format_map(vars())
print(fm)

class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n

a = Info('hyr',999999999999)
print(vars(a))
fm_2 = s.format_map(vars(a))
print(fm_2)

class safesub(dict):
    def __missing__(self,key):
        return '{' + key + '}'

del n
fm_3 = s.format_map(safesub(vars()))
print(fm_3)

import sys
print(sys._getframe().f_locals)
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
