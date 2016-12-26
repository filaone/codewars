#!/usr/bin/python
#-*- coding:utf-8 -*-

s = ' Hello    World \n'
ss = s.strip()
print(ss)
ss = s.lstrip()
print(ss)
ss = s.rstrip()
print(ss)


t = '-------hello======'
print(t.strip('-'))
print(t.strip('-='))

print(s.replace(' ', ''))

import re
ss = re.sub(r'\s+',' ', s)
print(ss)
