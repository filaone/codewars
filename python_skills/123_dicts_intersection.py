#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 123_dicts_intersection.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 19:29:34
#Last Modifieda: 2016-10-06 19:29:34
#*********************************************************

d2 = {'b': 2, 'c': 3}
d1 = {'a': 1, 'b': 2}


set_d1 = set(d1.keys())
set_d2 = set(d2.keys())

print set_d1 & set_d2 # jiaoji

print set_d1 | set_d2 # bingji

print set_d2 - set_d1 # chaji

print "http://blog.csdn.net/business122/article/details/7541486"
print ""
