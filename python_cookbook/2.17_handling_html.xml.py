#!/usr/bin/python
#-*- coding:utf-8 -*-

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(ascii(p.unescape(s)))


from xml.sax.saxutils import unescape
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
