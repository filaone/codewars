#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 094_replace_element_of_the_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 22:41:28
#Last Modifieda: 2016-10-03 22:41:28
#*********************************************************

l = "hello world this is a new string".split()
print l

l2 = map(lambda x: x.capitalize(), l)
print l2

l3 = l*10
print l3

l4 = [1]* 10
print l4

l[1:3] = ['change'] * 2
print l
