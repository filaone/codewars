#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 070_valid_regexp.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-25 18:18:08
#Last Modifieda: 2016-09-25 18:18:08
#*********************************************************

import re

def valid_regexp(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

string_1 = "abcdef\s\s\s\s"
string_2 = "##*&^*()*(*^%&(^(*"

print valid_regexp(string_1)
print valid_regexp(string_2)
