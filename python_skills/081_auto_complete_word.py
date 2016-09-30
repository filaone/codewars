#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

class youCompleteMe():
    def __init__(self,words):
        self.words = list(words)
        c_words = [];
        self.createDict(self.words)
    def complete_1(self, head):
        self.c_words = []   
        for ele in self.words:
            if re.compile(head).search(ele):
                self.c_words.append(ele)
        return self.c_words
    def complete_2(self,head):
        if self.dicts.has_key(head):
            return self.dicts[head]
        else:
            return "NO Words!"
            # if not return somthing the out side print will print "None"

    def createDict(self, words):
        for ele in words:
            for i in range(len(ele)):
                if self.dicts.has_key(ele[:i+1]):
                    self.dicts[ele[:i+1]].append(ele)
                else:
                    self.dicts[ele[:i+1]] = []
                    self.dicts[ele[:i+1]].append(ele)
        print self.dicts
    words = [];
    c_words = [];
    dicts = dict("");

word_test = "this is my test cp mk config con mm dd df break bre".split(" ")

completer = youCompleteMe(word_test)
print completer.complete_1("br")
print completer.complete_2("br")
print "3",completer.complete_1("hello")
print "4",completer.complete_2("hello")
print "5",completer.complete_1("thi")
print "6",completer.complete_2("thi")
print completer.complete_1("c")
print completer.complete_2("c")
print completer.complete_1("m")
print completer.complete_1("br")
