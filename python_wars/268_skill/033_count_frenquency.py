#!/usr/bin/python
#-*- coding:utf-8 -*-

from collections import defaultdict
from collections import Counter
from itertools import groupby
import json

string_1 = u"sdlkghweoivnlskdguoqeithosdkhgja;sldnasodfiuasldhg;qieuwouhydhgfjsdkljgslkdfjgslkfdjgslkfdjdgfskdfjTö äåii差距就在这希 lllll 望您能集体 反思最后觉定 ... き ki , ひ hi , み mi, け ke, へ he, め me, こ ko, そ so, と to, の no, も mo, よ yo"
string_2 = u"ö äåii差距就在这希 lllll 望您能集体 反思最后觉定 ... き ki , ひ hi , み mi, け ke, へ he, め me, こ ko, そ so, と to, の no, も mo, よ yoy"

result = defaultdict(int)
words_1 = string_1.split()
print words_1
for word in words_1:
    result[word] += 1
    print word.encode('utf-8')

print result

print result.keys()
for key in result.keys():
    print key.encode('utf-8')

result_2 = dict((key, len(list(group))) for key, group in groupby(sorted(words_1)))
print result_2

freqs_1 = Counter(words_1)
print freqs_1


freqs_2 = {}
for word in words_1:
    freqs_2[word] = freqs_2.get(word, 0) + 1
print freqs_2
