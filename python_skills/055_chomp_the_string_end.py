#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
string_1 = "\n\nline \n\n\n\n line2\n\n\n\n line3\n\n\n"
print "------"
print string_1
print "------"
print re.sub(re.compile(r'\s+\Z'),"",string_1)
print "------"
print string_1.rstrip()
print "------"
