#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 095_get_random_element_from_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 22:50:03
#Last Modifieda: 2016-10-03 22:50:03
#*********************************************************

import random
l = [random.randint(1,100)] * 100
l = map(lambda x: random.randint(1,100), l)

print l[random.randint(0,len(l))]
