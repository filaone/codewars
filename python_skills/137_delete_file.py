#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import shutil

print "http://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python"
if not os.path.exists("./addon/137"):
    os.mkdir("./addon/137")
if not os.path.exists("./addon/137/empty"):
    os.mkdir("./addon/137/empty")
shutil.copy(__file__,"./addon/137/"+__file__)
shutil.copy(__file__,"./addon/137/"+__file__+"_1")
shutil.copy(__file__,"./addon/137/"+__file__+"_2")
shutil.copy(__file__,"./addon/137/"+__file__+"_3")

print "remove file"
os.remove("./addon/137/"+__file__)

print "remove empty diretory"
os.rmdir("./addon/137/empty")

print "remove directory and all its contents"
shutil.rmtree("./addon/137")
