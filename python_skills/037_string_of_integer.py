#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 037_string_of_integer.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-08-25 22:38:55
#Last Modifieda: 2016-08-25 22:38:55
#*********************************************************

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print RepresentsInt("11234")
print RepresentsInt("11.234")
print RepresentsInt("11l234")
print RepresentsFloat("11234")
print RepresentsFloat("0.11234")


print "isdigit"
print "hello".isdigit()
print "1.2".isdigit()
print "12".isdigit()
