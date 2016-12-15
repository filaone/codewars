#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 212_user_and_group_id.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-14 11:02:17
#Last Modifieda: 2016-12-14 11:02:17
#*********************************************************

import os,getpass
import pwd
import grp
# pwd struct : (pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell)
# grp struct : (gr_name, gr_passwd, gr_gid, gr_mem)

user = 'Alex'

mygroup = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
print mygroup
myuser =  [u.pw_name+str(u.pw_uid) for u in pwd.getpwall() if 'zsh' in u.pw_shell]
print myuser

print pwd.getpwuid(501)
print pwd.getpwnam('Alex').pw_uid

print grp.getgrgid(501)
print grp.getgrnam('admin')
print "http://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn"


# get the current user and group
print "Current user is : ",pwd.getpwuid(os.getuid()).pw_name
print "Current user is : ",getpass.getuser()
print "Current group is: ",grp.getgrgid(os.getgid()).gr_name
print "http://stackoverflow.com/questions/3042304/how-to-determine-what-user-and-group-a-python-script-is-running-as"
