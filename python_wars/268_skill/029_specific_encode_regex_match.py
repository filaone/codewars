#!/usr/bin/python
#-*- coding:utf-8 -*-
import re

print "http://stackoverflow.com/questions/10165102/how-do-i-get-a-regular-expression-to-recognize-non-ascii-characters-as-letters"
print "Always work in unicode, and only convert to an encoded representation when necessary."

string_1 = u"ö äåii差距就在这希 lllll 望您能集体 反思最后觉定 ... き ki , ひ hi , み mi, け ke, へ he, め me, こ ko, そ so, と to, の no, も mo, よ yo"
string_2 = "ö äåii差距就在这希 lllll 望您能集体 反思最后觉定 ... き ki , ひ hi , み mi, け ke, へ he, め me, こ ko, そ so, と to, の no, も mo, よ yo"

print string_1

print re.findall(r'\w+', string_1)
re_1 = re.findall(r'\w+', string_2.decode('utf-8'), flags=re.U)
print "Use flags re.UNICODE"
re_2 = re.sub(r'[\w]+', '', string_2.decode('utf-8'), flags=re.U)
for m in re_1:
    print m.encode('utf-8')
print re_2
