#!/usr/bin/python
#-*- coding:utf-8 -*- 

import re

def tabify(s, tabstop = 8):
    return re.sub(re.compile(ur' '*tabstop), "\t", s)

def untabify(s, tabstop = 8):
    return re.sub(re.compile(ur"\t"), " "*tabstop, s)

# 1. Add indent for each line 
def indent0(s, n):
    return re.sub(re.compile(r'^'), " "*tabstop, s)

# 2. new tabify for each line
def indent(s, n):
    return re.sub(re.compile(r'^'), "\t"*n, s)

tabify_file = open("./058_change_indent_wtc_.py")
for line in tabify_file:
    new_str = indent(line, 3)
    print new_str
