#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 084_copy_ltsd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 16:29:28
#Last Modifieda: 2016-10-03 16:29:28
#*********************************************************
import copy

l = ['a','b','c','d','e']
t = ('a','b','c','d','e','e')
s = set(['a','b','c','d','e','e',])
d = {'a':1, 'b':2, 'c':3}



# 1.1 copy
l2 = l
l2[1] = 'l2change'
print l

# 1.2 you can see l changes when l2 changed
l3 = l[:]
l3[0] = 'l3change'
l4 = list(l)
l4[2] = 'l4change'
l5 = copy.copy(l)
l5[3] = 'l5change'
print l

# 2.1 tuple copy tuple cannot be modify so copy make no sense

# 3.1 set copy set has no order cannot use [:]
s2 = set(s)
s3 = copy.copy(s)
print s3
print s2

# 4.1 dict has no order cannot use [:]
d2 = dict(d)
d3 = copy.copy(d)
print d2, d3
