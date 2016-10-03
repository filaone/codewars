#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 086_deal_all_the_elem_ltsd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 17:00:03
#Last Modifieda: 2016-10-03 17:00:03
#*********************************************************

l = ['a','b','c','d','e']
t = ('a','b','c','d','e','e')
s = set(['a','b','c','d','e','e',])
d = {'a':1, 'b':2, 'c':3}

for ele in l:
    print ele

for ele in d:
    print ele,d[ele]

for ele in s:
    print ele

for ele in t:
    print ele
