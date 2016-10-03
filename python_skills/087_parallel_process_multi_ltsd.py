#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 087_parallel_process_multi_ltsd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 17:14:04
#Last Modifieda: 2016-10-03 17:14:04
#*********************************************************

l1 = ['1','b','c','d','e','f']
l2 = ['a','2','3','4','5','6']

print zip(l1,l2)

for ele in zip(l1,l2):
    print ele[1],"---",ele[0]


