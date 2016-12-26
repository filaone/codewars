#!/usr/bin/python
#-*- coding:utf-8 -*-

# 2.05 Searching and Replaceing Text

# For Simple literal patterns, use str.replace()
text = "yeah, bu no, but yeah, but no, but yeah!"
text.replace('yeah', 'yep')


# For complicated patterns, use the sub() function/methods in the re module
text = "Today is 11/22/33, pyCon starts at 3/13/2013."
import re
new_text = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2', text)
print(new_text)

# if need repeat please comiple first
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2',text))

# want to know how many substitutions
new_text, n  = datepat.subn(r'\3-\1-\2', text)
print(new_text,n)
