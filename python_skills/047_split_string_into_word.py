#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

string_1 = "You can remove the empty element with The list comprehension(or just The regular for loop)"

print string_1.split()
print string_1.split('the')
print string_1.split(r'The')
pattern_1 = re.compile(r"the")
print re.split(pattern_1,string_1)
