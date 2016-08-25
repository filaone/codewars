#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
string_1 = "A1B2C3C3D4G5J88I9870897\n C1N200J1\n a1B2\n A10B\n"
pattern_1 = re.compile(r'([A-Z]\d+)+')

print "determine have pattern or not"
if pattern_1.match(string_1):
    print "matched"
else:
    print "not match"

string_2 = u'A1B2C3C3D4G5J88I9870897'
pattern_2 = re.compile('([A-Z]\d)+')


print "the first location of the pattern"
for m in re.finditer(pattern_2,string_1):
    print m.group()
for m in pattern_2.finditer(string_1):
    print m.start(),m.end(), m.group()

callable_iterator_object  = pattern_2.finditer(string_1)
print callable_iterator_object
print list(callable_iterator_object)[2].group()
print callable_iterator_object
#print list(callable_iterator_object)[2].group()
# why error????
re_matchobject = pattern_2.search(string_2)
print "only the first span [0,14)"
print re_matchobject
print re_matchobject.group()
print re_matchobject.span()


print "the last location of the pattern"
print "can use finditer to create a new list and use [-1]"
print "just use the finditer"

print "get more information"
print "use m.start(),m.end(),m.group()"

print "process the target lines"
print string_1
print pattern_1.findall(string_1)
print re.findall(pattern_1, string_1)
f = open('/home/wsg/Code/python_project/268_skill/020_text_encoding.py')
for line in f:
    print line
    print  pattern_2.findall(string_1)
f.close()
