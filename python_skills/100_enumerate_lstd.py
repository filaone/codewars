#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 100_enumerate_lstd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 23:53:28
#Last Modifieda: 2016-10-03 23:53:28
#*********************************************************
# http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
l = range(1,10)
for idx,val in enumerate(l):
    print idx,val
