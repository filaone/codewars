#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 068_hide_particular_string.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-22 22:20:21
#Last Modifieda: 2016-09-22 22:20:21
#*********************************************************
import re

string_1 = "password:helloworld"
string_2 = "password:hello"

def replace_parti(s):
    m = re.match(re.compile(r"(password:)(.*)"),s)
    length = len(str(m.group(2)))
    print length
    return re.sub(re.compile(r"(password:)(.*)"),'{}{}'.format(r"\1","*"*length), s)

print replace_parti(string_1)
print replace_parti(string_2)

# 第一没有意识到 /1 要和r一定要联合起来用
# 第二没有意识到 ‘{}’和 format联合使用
# 第三没有意识到 r"\1"放在len里面就失效了

