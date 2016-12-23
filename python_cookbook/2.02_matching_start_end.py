#!/usr/bin/python 
#-*- coding:utf-8 -*-

filename = "spam.txt"
print(filename.endswith('.txt'))
print(filename.startswith('spam'))

import os
filenames = os.listdir('.')

# endswith startswith accept tuple
cpp_file = [name for name in filenames if name.endswith(('.c','.py'))]
print(cpp_file)

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

baidu = read_data('http://www.baidu.com')


print(filename[-4:] == '.txt')

import re
print(re.match('spam', filename))

