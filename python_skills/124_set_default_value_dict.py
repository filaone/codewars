#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 124_set_default_value_dict.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 19:55:54
#Last Modifieda: 2016-10-06 19:55:54
#*********************************************************

from collections import defaultdict

d2 = dict()
d2 = defaultdict(lambda:-1, d2)
print d2['helo']
print "http://stackoverflow.com/questions/9139897/how-to-set-default-value-to-all-keys-of-a-dict-object-in-python"
