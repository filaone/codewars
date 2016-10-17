#!/usr/bin/python
#-*- coding:utf-8 -*-

import fileinput

class FileLineWrapper(object):
    def __init__(self,f):
        self.f = f
        self.line = 0
    def close(self):
        return self.f.close()
    def readline(self):
        for line in self.f:
            self.line += 1
        return self.line


f = FileLineWrapper(open(__file__,'r'))
print f.readline()
print f.line
