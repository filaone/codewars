#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 116_delete_dict_element.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 16:52:46
#Last Modifieda: 2016-10-04 16:52:46
#*********************************************************

d = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b

del d[chr(97)]
print d
print "http://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary"

d.clear()
print d
