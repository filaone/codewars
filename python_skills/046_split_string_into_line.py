#!/usr/bin/python
#-*- coding:utf-8 -*-

string_1 = "a\nb\nc\nd\ne\n"
print list(string_1)
print string_1.splitlines()

lines  = open('./019_literal.py').readlines()
print lines
clean_lines = [x.strip() for x in lines]
print clean_lines

