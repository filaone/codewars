#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
string_1 = "foo foo. {foo}"
string_2 = "foo3 hfoo foobar!"
string_3 = u'This is\ta 2pen.'
pattern_1 = re.compile(r'\bfoo\b')
print pattern_1.findall(string_1)
print pattern_1.findall(string_2)
print re.findall(r'\w+', string_2)
print re.findall(r'\w+', string_3)
print string_3.split()
