#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
print os.getcwd()

os.chdir("/tmp/")
# print current work directory
print os.getcwd()

os.chdir(os.getcwd()+"/../etc")
print os.getcwd()
