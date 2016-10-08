#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 128_split_file_name.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-07 10:36:05
#Last Modifieda: 2016-10-07 10:36:05
#*********************************************************

import os

f = "/foo/bar/test/128.rb"
print os.path.splitext(f)
print os.path.splitext(os.path.basename(f))
print os.path.basename(f)
print os.path.dirname(f)

print os.path.join('c:\\','csv','test.csv')
print os.path.join('/home/aa','/home/aa/bb','/home/aa/bb/c')
print "http://wangwei007.blog.51cto.com/68019/1104940"
