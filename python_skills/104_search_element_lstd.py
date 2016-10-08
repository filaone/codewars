#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 104_search_element_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 15:08:24
#Last Modifieda: 2016-10-04 15:08:24
#*********************************************************

l = range(1,11)
# x in list
print (1 in l)
# find a colletciton
matches = [x for x in l if x == 1]
print matches
# find location
print l.index(1)
print "http://stackoverflow.com/questions/9542738/python-find-in-list"
