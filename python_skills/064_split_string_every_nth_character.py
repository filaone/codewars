#!/usr/bin/python
#-*- coding: utf-8 -*-

import re

string = "1234567890"
# split into list [12,34,56,78,90]

def  split_nchars(s,n):
    pattern = ".{1,"+str(n)+"}"
    return re.findall(re.compile('.{%d,%d}'%(1,n)),s)
    # error because re use {}return re.findall(re.compile('.{{0},{1}}'.format(1,n)),s)
    #return re.findall(re.compile(pattern),s)

print split_nchars(string,3)
print split_nchars(string,2)
print split_nchars(string,4)
