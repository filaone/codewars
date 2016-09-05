#!/usr/bin/python
#-*- coding:utf-8 -*-
#**********************************************************
#Filename: 052_replace_part_of_string.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-05 22:58:15
#Last Modifieda: 2016-09-05 22:58:15
#*********************************************************
import re

string_1 = "这是一首简hello 单 hello 地小小小小情歌，哦哦".decode('utf-8')
print "https://www.zhukun.net/archives/6397"
print string_1.replace(u'小',u'大')

print string_1

pattern = re.compile(u'小')
string_2 = pattern.sub(u'大',string_1)
print string_2
