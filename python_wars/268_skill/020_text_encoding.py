#!/usr/bin/python
# -*- coding: utf-8 -*-

print u"The default for Python 2 is ASCII(for Python 3 it's utf-8)."
print u"This just affects how the interpreter reads the characters in the file."
print u"When you declare a string with a u in front, like u'This is a string', it tells the Python compiler that the string is Unicode, not bytes. the most different is that youcan now embed unicode characters in the strng(that is, u'\u2665' is now legal, you can use from __futrue__ import unicode_literals to make it the default."
print b'\u2665' u'\u2665'
