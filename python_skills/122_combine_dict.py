#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 122_combine_dict.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 19:10:14
#Last Modifieda: 2016-10-06 19:10:14
#*********************************************************

import copy
print "http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression"
d = dict()
d2 = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b
    d2[b]=a

z = d.copy()
z.update(d2)
print z
