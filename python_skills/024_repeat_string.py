#!/usr/bin/python
#-*- coding: utf-8 -*-

s = "hello world"

print s[:6]*2
print 2*s
print ' '.join((s[:]) * 2)
print ' '.join([s[:]] * 2)
