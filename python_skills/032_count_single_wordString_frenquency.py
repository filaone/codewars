#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

        
string_1 = "abcdsdfsdfs\ndskjghwer\basdjtwoieutuwet\s"
pattern_1 = re.compile(r"a")
print pattern_1.findall(string_1)
print len(pattern_1.findall(string_1))

print string_1.count('a')
