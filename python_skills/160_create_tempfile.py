#!/usr/bin/python
#-*- coding:utf-8 -*-

import tempfile
import os

print "https://docs.python.org/2/library/tempfile.html"
print "http://stackoverflow.com/questions/23452361/cant-use-fdopen-with-mkstemp"
#tempfile.mkdtemp('/tmp/160_dir','temp')
#tempfile.mkstemp('/tmp/160_dir/a','temp')
#tempfile.mkstemp('/tmp/160_dir/b','temp')


tempfile_c = tempfile.TemporaryFile('w+b', -1, 'suffix',"prefix",'/tmp/');
print "tempfile_c : ",tempfile_c.name
os.system("tree /tmp")


tempfile_c.write("Hello World_0!")
tempfile_c.write("Hello World_1!")
tempfile_c.write("Hello World_2!")
tempfile_c.seek(0)
for line in tempfile_c:
    print line.strip()

os.system("tree /tmp")

tempfile_d = tempfile.NamedTemporaryFile(suffix = "suffix", prefix = "prefix", dir = "/tmp")
print "tempfile_d : ",tempfile_d.name

tempfile_e = tempfile.mkstemp(suffix = "_suffix", prefix = "prefix_", dir = '/tmp')
print tempfile_e
os.remove(tempfile_e[1])

tempfile_dir_a = tempfile.mkdtemp(prefix = 'temp_', dir = '/tmp/')
print tempfile_dir_a
tempfile_f = tempfile.mkstemp(prefix = "temp_", dir = tempfile_dir_a)
print "tempfile_f : ",tempfile_f[1].strip()
tempfile_f_name = tempfile_f[1].strip()
tempfile_f_file = open(tempfile_f_name,'r+w+');
tempfile_f_file.write("Hello World_11!")
tempfile_f_file.write("Hello World_22!")
tempfile_f_file.seek(0)
buffer_f = tempfile_f_file.readlines()
print buffer_f
os.remove(tempfile_dir_a)
