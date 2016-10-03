#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 093_delete_ele_begin_end_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 19:12:36
#Last Modifieda: 2016-10-03 19:12:36
#*********************************************************

l = [1,2,3,4,5,6,7]
l2 = l[1:]
l3 = l[:-1]
print l3, l2
l3.pop()
l3.pop(0)
print l3
