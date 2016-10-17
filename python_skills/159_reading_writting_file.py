#!/usr/bin/python
#-*- coding:utf-8 -*- 

import os
import time

print "https://docs.python.org/2/library/stdtypes.html?highlight=seek#file.seek"

with open("./addon/159_reading","a+") as f:
    print f.readline().strip()
    f.seek(0, os.SEEK_END) 
    while True:
        f.seek(0, os.SEEK_CUR)
        data = f.readline().strip()
        if data:
            print data.strip()
        time.sleep(0.1)
