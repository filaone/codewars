#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 197_format_time.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 17:46:51
#Last Modifieda: 2016-11-02 17:46:51
#*********************************************************

import time
print time.strftime("%Y-%M-%S",time.localtime(time.time()-1000))
