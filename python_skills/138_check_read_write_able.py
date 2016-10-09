#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import stat
from pwd import getpwuid

print "http://stackoverflow.com/questions/1861836/checking-file-permissions-in-linux-with-python"


print os.access(__file__,os.R_OK)
print os.access(__file__,os.W_OK)
print os.access(__file__,os.X_OK)


print os.stat(__file__)
st = os.stat(__file__)
print bool(st.st_mode & stat.S_IRGRP)

print "http://stackoverflow.com/questions/1830618/how-to-find-the-owner-of-a-file-or-directory-in-python"
print getpwuid(os.stat(__file__).st_uid).pw_name
print os.stat(__file__).st_uid

print getpwuid(1000)
