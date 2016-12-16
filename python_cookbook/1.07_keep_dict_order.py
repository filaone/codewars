#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.07_keep_dict_order.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-16 17:11:13
#Last Modifieda: 2016-12-16 17:11:13
#*********************************************************

# 1.07 Keeping Dictionaries in Order

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] =3
d['grok'] =4

for key in d:
    print(key,d[key])
