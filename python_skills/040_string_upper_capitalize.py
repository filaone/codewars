#!/usr/bin/python
#-*- coding: utf-8 -*- 

string_1 = "abcdJGUYB"
string_2 = "sdgIDJdf sdjg222jsd def"

print string_1.upper()
print string_1.lower()
print string_1.swapcase()

print string_2.title()
print string_2.capitalize()
def canonical_header_name(str):
    return "-".join(map(lambda x:x.capitalize(),str.split("-")))

string_3 = "wang-shu-guang"
print canonical_header_name(string_3)
