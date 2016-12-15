#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 213_switch_user_group.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-14 11:33:54
#Last Modifieda: 2016-12-14 11:33:54
#*********************************************************

import pwd, grp, os

current_name = pwd.getpwuid(os.getuid()).pw_name
print "current uid : ",current_name
newuid = pwd.getpwnam('cnetwork').pw_uid
current_name = "cnetwork"
#os.setuid(newuid)
#current_name = pwd.getpwuid(os.getuid()).pw_name
#print "current uid : ",current_name

# error once you give up root, it's gone
#os.setuid(pwd.getpwnam('root').pw_uid)
#current_name = pwd.getpwuid(os.getuid()).pw_name
#print "current uid : ",current_name

path = os.path.dirname(os.path.realpath(__file__))+"/"+__file__
print path
os.chown(path, pwd.getpwnam(current_name).pw_uid , pwd.getpwnam(current_name).pw_gid)
print "http://www.cnblogs.com/peida/archive/2012/12/04/2800684.html"
print "http://stackoverflow.com/questions/5994840/how-to-change-the-user-and-group-permissions-for-a-directory-by-name"
