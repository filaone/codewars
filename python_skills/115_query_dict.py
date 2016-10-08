#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 115_query_dict.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 16:44:34
#Last Modifieda: 2016-10-04 16:44:34
#*********************************************************

x = [chr(x) for x in range(97,111)]
y = range(97,111)
d = dict()
for a,b in zip(x,y):
    d[a] = b

print d

for i in range(96, 99):
    if chr(i) in d:
        print "found!"
    else:
        print "not found"
