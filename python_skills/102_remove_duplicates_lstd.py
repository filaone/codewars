#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 102_remove_duplicates_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 14:54:02
#Last Modifieda: 2016-10-04 14:54:02
#*********************************************************

import random
print "http://stackoverflow.com/questions/7961363/removing-duplicates-in-lists"
l = [random.randint(1,100) for i in range(1,101)]
print l
l2 = list(set(l))
print l2
