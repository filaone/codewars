#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 198_string_to_time.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-04 16:00:10
#Last Modifieda: 2016-12-04 16:00:10
#*********************************************************

from datetime import datetime
date_object = datetime.strptime("Jun 1 2005 1:33PM", '%b %d %Y %I:%M%p')
now = datetime.now()
print now.strftime("%Y-%m-%d %H:%M:%S %I %p")
print date_object
print "http://stackoverflow.com/questions/466345/converting-string-into-datetime"

from dateutil import parser
dt = parser.parse("Jun 1 2005 1:33PM")
print dt
