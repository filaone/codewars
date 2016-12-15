#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 201_last_day_of_months.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-04 17:50:56
#Last Modifieda: 2016-12-04 17:50:56
#*********************************************************

import calendar
print calendar.monthrange(2002,1)
print calendar.monthrange(2016,2)
print calendar.monthrange(2016,12)
print calendar.monthrange(2017,2)

print "returns weekday of first day of the month and number of days"
print "http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python"
