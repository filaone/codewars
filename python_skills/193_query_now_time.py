#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 193_query_now_time.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 17:12:52
#Last Modifieda: 2016-11-02 17:12:52
#*********************************************************

import time
print time.strftime("%H:%M:%S",time.localtime())
print time.strftime("%Y:%m:%d",time.localtime())
print time.localtime()
print time.localtime().tm_year

print "tm_year  is year, tm_month is 1-12 month number, tm_mday is 1-31 month day, tm_hour is 0-23 hour number"
print "tm_min, tm_sec, tm_wday is 0-6 and 0 is monday, tm_yday is 1-366 years day, tm_isdst is -1|0|1"
print "http://www.cnblogs.com/ITOps/p/5784244.html"
