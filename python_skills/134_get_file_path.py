#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

print "http://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python"
print os.path.abspath(__file__)

print "The os.path.realpath resolves symlinks and abspath doesn't"
print os.path.realpath(__file__)


