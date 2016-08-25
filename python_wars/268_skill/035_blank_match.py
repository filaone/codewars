#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

pattern_1 = re.compile(r' ')
string_1 = u"   \t\n\r\f"
print string_1
print string_1.count(r"\s")
print len(pattern_1.findall(string_1))

