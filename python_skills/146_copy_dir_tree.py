#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 146_copy_dir_tree.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 21:24:04
#Last Modifieda: 2016-10-10 21:24:04
#*********************************************************

import os
import shutil

path = os.path.realpath(__file__)
pwd = os.path.dirname(path)
filename = os.path.basename(path)
#os.path.copytree()
print path
print pwd
print filename

shutil.copytree("/Users/Alex/coding/code",pwd+"/addon/146_dir")
