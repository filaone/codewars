#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.03_keep_last_n_items.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-15 17:32:15
#Last Modifieda: 2016-12-15 17:32:15
#*********************************************************


# 1.03 Keeping the Last N Items
# http://stackoverflow.com/questions/13786797/python-subprocess-call-no-such-file-or-directory
# http://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python-subprocess-module/
# http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
# http://pyzh.readthedocs.io/en/latest/the-python-yield-keyword-explained.html
# 这里遇到的第一个难点是subprocess的使用
# p = subprocess.run(*(cmd.split()), shell=True, stdout = subprocess.PIPE)
# 第二个难点是如何如何在这里面用用history 因为hisotry 是组合命令‘fc -l 1’所以需要分开写
# 而且可能因为python用户并没有History的命令所以执行为空
# 第三个难点在于subprocess.stdout的格式是bytes必须经过decode转为str才能进行操作
# 第四个难点在于原代码中使用的是f = open()，可以使用for line in lines，但是对于字符串使用会产生单个字符的序列
# 所以在search函数中加入了一个判断是不是str
# list 长度 list.__len__() , len()只能用于str

import subprocess
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen = history)
    if type(lines) == str:
        lines = lines.split('\n')
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    cmd = 'ls /Users/Alex/coding/codewars/python_skills | tail -100'
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
    lines = p.stdout.read().decode('utf-8')
    print(lines)
    for line, previous_lines in search(lines,'pattern',3):
        for pline in previous_lines:
            print(pline, end = '')
        print(line, end = '')
        print('-'*20)
# discuss
    q = deque(maxlen = 4)
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    q.append(5)
    print(q)
    q.appendleft(6)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)

