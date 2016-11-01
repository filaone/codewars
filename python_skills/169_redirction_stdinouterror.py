#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 169_redirction_stdinouterror.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 16:53:18
#Last Modifieda: 2016-11-01 16:53:18
#*********************************************************

import sys
import fileinput

#sys.stdin = open("./addon/169_stdin",'r')
#sys.stdout = open("./addon/169_stdout",'w+')
#sys.stderr = open("./addon/169_stderr","w+")

print "-----------stdout-----------"
#print sys.stdin.read()
print len(sys.argv)
for ele in sys.argv:
    print ele
print "-----------stdout-----------"

for line in fileinput.input():
    print line
    print "*********"
print "cannot use python file.py < input_file to replace stdin, must write function process this file"
