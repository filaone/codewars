#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 131_glob_pathname_dir.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-07 15:09:45
#Last Modifieda: 2016-10-07 15:09:45
#*********************************************************

import glob

print glob.glob('./0[0-2][0-9]*.*')

# all file and dir
print glob.glob('**.**')

print "所有的jpg文件"
print glob.glob('**/*.jpg')

print "所有的Jpg 和md 文件"
print glob.glob('**/*.{jpg,md}')

print "所有目录"
print glob.glob('./**')


print glob.glob('')
print glob.glob('')
print glob.glob('')
print glob.glob('')
