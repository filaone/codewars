#!/usr/bin/python
#-*- coding: utf-8 -*-

string = u'Hello world #-*- coding: utf-8 -*- '
print "String Length : "+str(len(string))
list_s = list(string)
print len(list_s)
tuple_s = tuple(string)
tuple_l = tuple(list_s)
print tuple_s
print len(tuple_s)
print tuple_l
print len(tuple_l)
set_s = set(string)
set_l = set(list_s)
set_t = set(tuple_s)
print set_s
print len(set_s)

