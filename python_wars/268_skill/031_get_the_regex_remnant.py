#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
print "get the remnant of the match use re.sub()" 
s = "87 hel foo bar 87 foo"
r = re.compile(r"87\s")
print r.sub('',s)
print r.findall(s)
