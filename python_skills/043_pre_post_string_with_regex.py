#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

pattern_1 = re.compile(ur"(.*)论坛\|福彩(.*)")


string_1 = u"彩吧论坛- 首页_彩票论坛|福彩论坛|体彩论坛|3D彩票论坛"


print re.match(pattern_1, string_1).groups()
print re.match(pattern_1, string_1).group(1)
print re.match(pattern_1, string_1).group(2)

print "There is no pre_match and post_match in python"


