#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 092_add_ele_begin_end_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 19:07:24
#Last Modifieda: 2016-10-03 19:07:24
#*********************************************************

l = [1,2,3,4,5,6,7]
l.insert(0,0)
l[0:0] = [-1]
l = [-2] + l
print l
l.append(8)
print l
