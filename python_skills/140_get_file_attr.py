#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import stat

print os.stat(__file__)
statinfo = os.stat(__file__)
print statinfo[stat.ST_SIZE]

print "http://www.programcreek.com/python/example/14259/stat.ST_CTIME"
print "https://docs.python.org/3/library/stat.html"
# the stat.ST_UID is a list number
print statinfo[stat.ST_CTIME]
print statinfo[stat.ST_ATIME]
print statinfo[stat.ST_MTIME]
print statinfo[stat.ST_SIZE]

