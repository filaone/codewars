#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

print "http://stackoverflow.com/questions/8150745/regular-expression-how-to-match-a-string-containing-n-newline"
print "USE re.DOTALL"
print re.match(r".", "\n",re.DOTALL)
