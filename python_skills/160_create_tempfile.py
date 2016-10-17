#!/usr/bin/python
#-*- coding:utf-8 -*-

import tempfile

print "https://docs.python.org/2/library/tempfile.html"

tempfile.mkdtemp('160_dir','temp')
tempfile.mkstemp('./160_dir/a','temp')
tempfile.mkstemp('./160_dir/b','temp')



