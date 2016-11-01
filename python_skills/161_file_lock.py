#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 161_file_lock.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-31 20:08:20
#Last Modifieda: 2016-10-31 20:08:20
#*********************************************************

import fcntl
file_handle_1 = open("./addon/161_file","wr")
file_handle_2 = open("./addon/161_file","w+r+")

fcntl.flock(file_handle_1, fcntl.LOCK_EX)
file_handle_1.write("file_handle_1")
#file_handle_2.write("file_handle_2.1")
fcntl.flock(file_handle_1, fcntl.LOCK_UN)
fcntl.flock(file_handle_2, fcntl.LOCK_EX | fcntl.LOCK_NB)
file_handle_2.write("file_handle_2.2")
fcntl.flock(file_handle_2, fcntl.LOCK_UN)

print "http://tilde.town/~cristo/file-locking-in-python.html"
