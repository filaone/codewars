#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 196_plus_min_time.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 17:42:45
#Last Modifieda: 2016-11-02 17:42:45
#*********************************************************

import time
t1 = time.localtime(100000)
t2 = time.localtime(100010)
print t1
print t2

t1 = time.time()
print t1
t2 = t1 + (60*60*20*10)
print t2
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t2))
print t2 - t1
