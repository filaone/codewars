#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 167_delete_first_n.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 16:32:48
#Last Modifieda: 2016-11-01 16:32:48
#*********************************************************

lines = open(__file__).readlines()
open("./addon/167",'w').writelines(lines[3:-1])
print "http://stackoverflow.com/questions/2064184/remove-lines-from-textfile-with-python"
