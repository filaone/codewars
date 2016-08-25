#!/usr/bin/python
#-*- coding: utf-8 -*-

s = "Flügel"
print s
print "if no coding: utf-8 (use utf8 store the code)there is an error because ASCII has no ü"
print "u'' means this is a unicode string"
unicode_s = s.decode('utf-8')
print u"other_encode.decode('other_type') means turn the other string which use other type into the unicode"
print unicode_s

latin_s = unicode_s.encode('latin_1')
print u"unicode_string.encode('other') means turn unicode string into other encoding such as utf-8 or latin_1"
print latin_s

hanzi = '字瀛'
print hanzi
new_uni2 = u'字å­å字瀛'
print new_uni2
new_utf2 = new_uni2.encode('utf-8')
print new_utf2

