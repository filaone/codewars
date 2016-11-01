#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 164_binary_write_file.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 14:48:54
#Last Modifieda: 2016-11-01 14:48:54
#*********************************************************

import os

with open(__file__, "rb") as f:
    contents = f.readlines()
    f.close()
with open("./addon/164","wt") as f:
    f.write("".join(contents))
    f.close()

print contents
#os.system("cat ./addon/164")
with open("./addon/164","rb") as f:
    for line in f:
        print line.strip()

print "Windows process file differnt with linux , when write window add 0x0d before 0x0a, when read delete 0x0d before 0x0a, use b wb rb r+b the windows does not do anything with the file"
print "https://www.hitoy.org/binary-vs-text-mode.html"
