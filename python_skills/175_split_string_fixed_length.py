#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 175_split_string_fixed_length.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 01:04:10
#Last Modifieda: 2016-11-02 01:04:10
#*********************************************************

def split_string(string,n):
    return [string[i:i+n] for i in range(0,len(string),n)]

print ",".join(split_string("hellohellohellohelooheleee",5))
print "http://stackoverflow.com/questions/6372228/how-to-parse-a-list-or-string-into-chunks-of-fixed-length"
