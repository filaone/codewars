#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 072_multi_regexp_with_one_string.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-25 19:35:44
#Last Modifieda: 2016-09-25 19:35:44
#*********************************************************

import re
# match only at the begging of the string
def  multi_regexp(s):
    if re.search(pattern_1,s) and re.search(pattern_2,s):
        return True
    else:
        return False

pattern_1 = re.compile(r"设计")
pattern_2 = re.compile(r"程序")
pattern_3 = re.compile(r"wang")
pattern_4 = re.compile(r"设计|程序")
string_1 = "程序设计指南wang"
string_2 = "城设计需指南"

print re.search(pattern_1,string_1)
print re.search(pattern_3,string_1)
print re.search(pattern_4,string_1)

print multi_regexp(string_1)
print multi_regexp(string_2)
