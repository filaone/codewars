#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
s_list = re.findall('python', text, flags=re.IGNORECASE)
print(s_list)


# use support function
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

s_list = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(s_list)
s_list = re.sub('python', lambda x:x.group().upper(), text, flags=re.IGNORECASE)
print(s_list)
