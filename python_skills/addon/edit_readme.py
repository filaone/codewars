#!/usr/bin/python
#-*- coding:utf-8 -*-
#**********************************************************
#Filename: edit_readme.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-02 10:18:57
#Last Modifieda: 2016-10-02 10:18:57
#*********************************************************

with open('./README.md',"rw+") as readme:
    contents = readme.readlines()
readme.close()

i = 72
while(i <= 299):
    print  '|'+str(i - 41).zfill(3)+'||'
    contents.insert(i,'|'+str(i - 31).zfill(3)+'||\n')
    i += 1

with open('./README.md',"w") as readme:
    contents = "".join(contents)
    readme.write(contents)
readme.close()
