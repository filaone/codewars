#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

string = "2ksdbgjlkbn"
str_list = list(string)
str_list.insert(4,"-")
string2 = "".join(str_list)
print string2

print string[0:4] + "-" + string[4:]

string3 = re.sub(re.compile("(db)"),r"\1\1",string)
print string3
