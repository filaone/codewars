#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 163_insert_line_in_file.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 14:15:49
#Last Modifieda: 2016-11-01 14:15:49
#*********************************************************

import os

f = open(__file__, 'r')
contents = f.readlines()
f.close()

with open(__file__,'r') as f:
    contents = f.readlines()
    f.close()

contents.insert(0,"Hello World! Index 0 \n")
contents.insert(3,"Hello World! Index 3 \n")
contents.insert(-1,"Hello World! Index 3 \n")
contents.append("Hello World! Append\n")
f = open("./addon/163_write",'w')
contents = "".join(contents)
f.write(contents)
f.close()
os.system("cat ./addon/163_write")
print "http://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python"
