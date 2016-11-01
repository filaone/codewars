#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 172_format_number.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 22:48:59
#Last Modifieda: 2016-11-01 22:48:59
#*********************************************************

print "%d" % 2
print "%3d" % 2
print "%03d" % 2
print "%-8d" % 2
print "%.8d" % 2
print "%10.8d" % 2
print "%-10.8d" % 2



print "%x, %#x" %(100,100)
print "%o, %#o" %(100,100)
#print "%b, %#b" %(10,10)
print "%x, %#x" %(-100,-100)
print "%o, %#o" %(-100,-100)
