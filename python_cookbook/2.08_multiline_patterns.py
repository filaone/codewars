#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
comment = re.compile(r'/\*(?:.*?)\*/')
text1 = '/* This is a comment */'
text2 = '''/* This is a comment 
            multiline comment */
        '''
print("Stage 1")
print(comment.findall(text1))
print(comment.findall(text2))

print("Stage 2")
comment = re.compile(r'/\*(?:(?:.|\n)*?)\*/', re.DOTALL)
print(comment.findall(text2))
print("Stage 3")

comment = re.compile(r'/\*(?:.*?)\*/', re.DOTALL)
print(comment.findall(text2))
