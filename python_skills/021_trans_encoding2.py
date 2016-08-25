#!/usr/bin/python

new_s = '\xe5\xad\x97'
print type(new_s)
print new_s
new_uni = new_s.decode('latin_1')
print new_uni

new_utf = new_uni.encode('utf-8')
print new_utf
new_uni2 = new_s.decode('utf-8')
print new_uni2

new_uni3 = new_s.decode('gb2312','ignore')
print new_uni3

print "decode poduce unicode"
print "encode accept unicode"


