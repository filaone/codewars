#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 118_display_hash_inorder.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 10:56:18
#Last Modifieda: 2016-10-06 10:56:18
#*********************************************************

from collections import OrderedDict
import json

d2 = OrderedDict()
d = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b
    d2[a] = b

# show directly
print d
print json.dumps(d2)


