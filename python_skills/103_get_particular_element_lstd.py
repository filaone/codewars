#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 103_get_particular_element_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 14:57:35
#Last Modifieda: 2016-10-04 14:57:35
#*********************************************************

l2 = range(1,10)
print l2
odd_numbers = [y for x,y in enumerate(l2) if x%2 != 0]
print odd_numbers
