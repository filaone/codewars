#!/usr/bin/python
#-*- coding:utf-8 -*-
#**********************************************************
#Filename: 053_deal_with_caret_notation.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-05 23:22:00
#Last Modifieda: 2016-09-05 23:22:00
#*********************************************************
import re
string_1 = "take I'm a \ new \" man \" "

pattern_1 = re.compile(r'(["\'\\])')
string_2 = pattern_1.sub(r'\\\\\1',string_1)
print string_2
print "use sub and () and \\1"

pattern_2 = re.compile(r'\\\\([\\\'"])')
string_3 = pattern_2.sub(r'\1',string_2)
print string_3

pattern_3 = re.compile(r'(["\'\\])')
string_4 = pattern_3.sub(r'\1\1',string_1)
print string_4

pattern_4 = re.compile(r'([\'"\\])\1')
string_5 = pattern_4.sub(r'\1',string_4)
print string_5
