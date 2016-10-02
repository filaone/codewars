#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

pattern_1 = re.compile(r'.ython')
string_1 = 'i like python jython and dython (whatever that is)'

iterator = re.finditer(pattern_1, string_1)
match_tup = tuple(iterator)
print match_tup[1]
print match_tup[1].span()
print match_tup[1].start()
print match_tup[1].end()

print match_tup[1].end() - match_tup[1].start() + 1
print "use tuple contain the iterator"
