#!/usr/bin/python
#-*- coding:utf-8 -*-

# 2.12 Santizing and Cleaning Up Text
s = 'pýtĥöñ\fis\tawesome\r\n'
print(ascii(s))

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None  # Delete
}

a = s.translate(remap)

print(ascii(a))

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD',a)
print(ascii(b))
print(b.translate(cmb_chrs))
