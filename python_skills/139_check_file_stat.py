#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import stat

print "http://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python"
statinfo = os.stat(__file__)
print statinfo

# file exists
print os.path.exists(__file__)

# file size
print statinfo.st_size

# is file
# http://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python
print os.path.isfile(__file__)

# is dir
print os.path.isdir(__file__)


# is symblink
# http://stackoverflow.com/questions/11068419/check-if-file-is-symlink-in-python
print os.path.islink(__file__)
print stat.S_ISLNK(statinfo.st_mode)

print "https://docs.python.org/3/library/stat.html"
# is pipe 
print stat.S_ISFIFO(statinfo.st_mode)

# is socket
print stat.S_ISSOCK(statinfo.st_mode)

# is blockdev
print stat.S_ISBLK(statinfo.st_mode)

# is chardev
print stat.S_ISCHR(statinfo.st_mode)
