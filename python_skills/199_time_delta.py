#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 199_time_delta.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-04 17:33:18
#Last Modifieda: 2016-12-04 17:33:18
#*********************************************************

from datetime import datetime, timedelta

now = datetime.now()
new_date = now + timedelta(days = 100)
print new_date.strftime("%Y-%m-%d")

old_day = datetime.strptime("Jun 1 2003","%b %d %Y")
# delta is a timedelta object
delta = now - old_day
print delta.days
