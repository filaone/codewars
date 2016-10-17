#!/usr/bin/python
#-*- coding:utf-8 -*-

for line in (open(__file__, 'r')).readlines():
   print line.strip() 


for line in reversed(open(__file__, 'r').readlines()):
   print line.strip() 
