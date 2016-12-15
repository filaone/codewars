#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.05_priority_queue.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-15 22:38:54
#Last Modifieda: 2016-12-15 22:38:54
#*********************************************************

# 1.05 Implementing  a Priority Queue
# 压入的元素先变成一个tuple，并配合上-priority，这样能从大到小进行排列
# 取出的时候只取得[-1]即可

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1] if self.queue else []


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spa'), 9)
    q.push(Item('kan'), 7)
    q.push(Item('liu'), 0)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

