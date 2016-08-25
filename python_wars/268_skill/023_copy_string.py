#!/usr/bin/python
#-*- coding:utf-8 -*-
import copy

print "http://stackoverflow.com/questions/24804453/how-can-i-copy-a-python-string"



s = "This is a string"

a = str(s)
b = s[:]
c = s + ''
d = copy.copy(s)
e = s
f = (s + '.')[:-1]

print map(id, [s, a, b, c, d, e, f])
