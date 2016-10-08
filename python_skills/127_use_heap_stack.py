#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 127_use_heap_stack.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-07 09:59:11
#Last Modifieda: 2016-10-07 09:59:11
#*********************************************************

from collections import deque
# use list as heap 堆 FILO 先进先出
queue = deque([1,2,3])
queue.append(4)
queue.append(5)
print queue.popleft()
print queue.popleft()

# use list as stack 栈 LIFO 后进先出
stack = [1,2,3]
stack.append(4)
stack.append(5)
print stack.pop()
print stack.pop()
print "https://docs.python.org/2/tutorial/datastructures.html"
