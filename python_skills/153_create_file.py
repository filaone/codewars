#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

filename = "./addon/153_create"

if os.path.exists(filename):
    print "Files exists Create Error"
else:
    with open(filename,"w") as file:
        file.write((open(__file__,'r')).read())

print "http://stackoverflow.com/questions/18533621/error-when-creating-a-new-text-file-with-python"



