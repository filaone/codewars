#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 147_rm_dir_tree.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 21:35:29
#Last Modifieda: 2016-10-10 21:35:29
#*********************************************************

import os
import shutil

path = os.path.realpath(__file__)
pwd = os.path.dirname(path)
basename = os.path.basename(path)

shutil.rmtree(pwd+"/addon/146_dir/jumps")
print "http://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python"
