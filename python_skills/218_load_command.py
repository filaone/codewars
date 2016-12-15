#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 218_load_command.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-14 17:51:02
#Last Modifieda: 2016-12-14 17:51:02
#*********************************************************

import os
from glob import glob

os.system("ls")
os.system("ls | awk '{print $1\"hello\"}'")

import commands
print commands.getstatusoutput('wc -l 215*')
print commands.getstatusoutput('wc -l 218*')


# subprocess.check_output(*popenargs, **kwargs)
import subprocess
#sub_out = subprocess.Popen("ls -al 218_load_command.py".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#use glob
print "http://stackoverflow.com/questions/15965017/using-ls-in-python-subprocess-popen-function"
sub_out = subprocess.Popen('ls -al '.split() + glob('21*'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = sub_out.communicate()
print out
print err
print glob('21*')
