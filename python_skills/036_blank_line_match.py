#!/usr/bin/python
#-*- coding:utf-8 -*-

string_1 = """ 
a\n

b
  \n      
bbb\n
"""

file_1 = open('/home/wsg/Code/python_project/268_skill/032_count_single_wordString_frenquency.py')

for line in file_1:
    if not line.strip():
        print "a blank line"
    else:
        print line

print "---------------"
for line in string_1:
    print line
