#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 224_change_hostname_ip.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-14 19:14:30
#Last Modifieda: 2016-12-14 19:14:30
#*********************************************************

import socket

hostname = socket.gethostname()
IP = socket.gethostbyname("")
# gethostbyname is not work now
#IP = socket.gethostbyname(hostname)
IP = socket.gethostbyname(hostname)
print hostname+IP
