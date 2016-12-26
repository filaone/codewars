#!/usr/bin/python
#-*- coding:utf-8 -*- 

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no"'
text2 = 'Computer says "no." Phone says "yes."'

print(str_pat.findall(text1))

# * operator in a regular expression is greedy
print(str_pat.findall(text2))

# This makes the matching nongreedy. Not escape with the start or end text
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

