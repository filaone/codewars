#!/usr/bin/python
#-*- coding:utf-8 -*-

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
new_line = re.split(r'[;,\s]\s*',line)
print(new_line)
new_line = re.split(r'(;|,|\s)\s*',line)
print(new_line)
values = new_line[::2]
delimiters = new_line[1::2] + ['']
print(delimiters)
new_line = re.split(r'(?:;|,|\s)\s*',line)
print(new_line)
