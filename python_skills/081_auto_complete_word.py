#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

class youCompleteMe():
    def __init__(self,words):
        self.words = list(words)
        c_words = [];
    def complete_1(self, head):
        self.c_words = []   
        for ele in self.words:
            print ele
            if re.compile(head).search(ele):
                self.c_words.append(ele)
        return self.c_words

    words = [];
    c_words = [];

word_test = "this is my test cp mk config con mm dd df break bre".split(" ")

completer = youCompleteMe(word_test)
print completer.complete_1("br")
