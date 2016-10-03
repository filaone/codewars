#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 096_arrange_random_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 22:58:36
#Last Modifieda: 2016-10-03 22:58:36
#*********************************************************
import random

l = list(range(1,100))
print l

def arrage_Random(l):
    swap_index = 0
    for i in range(0,len(l)-1):
        swap_index = random.randint(i+1, len(l)-1)
        l[i],l[swap_index] = l[swap_index],l[i]
    return l

l = arrage_Random(l)

print l
