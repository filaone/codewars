#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 069_create_message_digest.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-25 17:25:45
#Last Modifieda: 2016-09-25 17:25:45
#*********************************************************

import sys
import hashlib

md5_method = hashlib.md5()
string_2 = hashlib.md5("Nobody inspects the spammish repetition").digest()
sha_method = hashlib.sha224()

# feed the method with update()
md5_method.update("Nobody inspects")
md5_method.update(" the spammish repetition")
if (string_2 == md5_method.digest()):
    print "YES, the update work"
else:
    print string_2
    print "md5_method.digest()"+md5_method.digest()
    print "Update is no same with directly digest"

sha_method.update("man tian fei wu, yi pian huang wu.")
print sha_method.hexdigest()
print hashlib.sha224("man tian fei wu, yi pian huang wu.").digest()

print "digest_size : "+str(md5_method.digest_size)
print "block_size : "+ str(md5_method.block_size)

# there is sha1, sha224, sha256, sha384 and sha512
string_1 = "Hello world!"

blo = "start"
while blo:
    # have to improve it
    blo = sys.stdin.read(12)
    sha_method.update(blo)
    print sha_method.digest()
print sha_method.digest()
