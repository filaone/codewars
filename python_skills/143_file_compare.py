#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 143_file_compare.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 10:51:28
#Last Modifieda: 2016-10-10 10:51:28
#*********************************************************

import os
import shutil
import filecmp

shutil.copy(__file__, "./addon/"+__file__)
print filecmp.cmp(__file__, "./addon/"+__file__)
dcresult =  filecmp.dircmp("./", "./addon/")
#print dcresult.report()
print dcresult.left
print dcresult.right
print dcresult.common
print "https://docs.python.org/2/library/filecmp.html"
print filecmp.cmp(__file__, "./addon")


