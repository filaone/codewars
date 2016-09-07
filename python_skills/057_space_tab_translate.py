#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

def replace_tab(s,tabstop = 4):
    result = str()
    for c in s:
        if c == '\t':
            result += ' '*tabstop
        else:
            result += c
    return result


string_1 = "hello \tw\to\tl\td\t\taaa"
string_2 = replace_tab(string_1)

def replace_tab_2(s,tabstop = 20):
    return re.sub(re.compile(r'\t'), ' '*tabstop, s)

string_3 = replace_tab_2(string_1)
print string_3


def tabify(s, tabstop = 20):
    return re.sub(re.compile(ur' '*tabstop), "\t", s)

print tabify(string_3)
