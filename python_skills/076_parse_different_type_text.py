#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 076_parse_different_type_text.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-25 20:49:51
#Last Modifieda: 2016-09-25 20:49:51
#*********************************************************

from urlparse import urlparse
import email

a = """From root@a1.local.tld Thu Jul 25 19:28:59 2013
Received: from a1.local.tld (localhost [127.0.0.1])
    by a1.local.tld (8.14.4/8.14.4) with ESMTP id r6Q2SxeQ003866
    for <ooo@a1.local.tld>; Thu, 25 Jul 2013 19:28:59 -0700
Received: (from root@localhost)
    by a1.local.tld (8.14.4/8.14.4/Submit) id r6Q2Sxbh003865;
    Thu, 25 Jul 2013 19:28:59 -0700
From: root@a1.local.tld
Subject: oooooooooooooooo
To: ooo@a1.local.tld
Cc:
X-Originating-IP: 192.168.15.127
X-Mailer: Webmin 1.420
Message-Id: <1374805739.3861@a1>
Date: Thu, 25 Jul 2013 19:28:59 -0700 (PDT)
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="bound1374805739"

This is a multi-part message in MIME format.

--bound1374805739
Content-Type: text/plain
Content-Transfer-Encoding: 7bit

ooooooooooooooooooooooooooooooooooooooooooooooo
ooooooooooooooooooooooooooooooooooooooooooooooo
ooooooooooooooooooooooooooooooooooooooooooooooo

--bound1374805739--"""

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print o.scheme
print o.port
print o.geturl()
print o.path
