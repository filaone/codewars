#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 098_query_elem_occurrence_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 23:32:59
#Last Modifieda: 2016-10-03 23:32:59
#*********************************************************

count = dict()
l = list(range(1,100))
for ele in l:
    if ele in count:
        count[ele] += 1
    else:
        count[ele] = 1
print count
