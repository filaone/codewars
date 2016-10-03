#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 097_query_lstd_length.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 23:21:11
#Last Modifieda: 2016-10-03 23:21:11
#*********************************************************

import random

l = map(lambda x: random.randint(1,100),list(range(1,100)))
print l

print len(l)
