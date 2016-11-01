#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 166_truncate_file.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 15:57:57
#Last Modifieda: 2016-11-01 15:57:57
#*********************************************************

import os

with open(__file__,"r") as f:
    print f.readline()
    contents =  f.readlines()
with open("./addon/166",'w+r') as f:
    f.write("".join(contents))
    f.flush()
    f.readline()
    f.seek(6)
    f.truncate(5)
    f.close()

os.system("cat ./addon/166")


print "why w and readline error"
