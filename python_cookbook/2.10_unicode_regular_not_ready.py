#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
num = re.compile(r'\d+')

nm = num.match("123")
print(nm.group())

new_nm = num.match('\u0661\u0662\u0663')
print(new_nm.group())

