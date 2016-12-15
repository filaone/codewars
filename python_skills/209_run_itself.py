#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 209_run_itself.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-12 22:15:36
#Last Modifieda: 2016-12-12 22:15:36
#*********************************************************

import time, threading

def myfunction_1(string, sleeptime, lock, *args):
    while( True ):
        lock.acquire()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s"
        lock.release()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s again"

def myfunction_2(string, sleeptime, lock, *args):
    while( True ):
        lock.acquire()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s"
        lock.release()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s again"

def myfunction_3(string, sleeptime, lock, *args):
    while( True ):
        lock.acquire()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s"
        lock.release()
        time.sleep(sleeptime)
        print string," sleep : ",sleeptime,"s again"

def main():
    lock = threading.Lock()
    our_thread_1 = threading.Thread (target = myfunction_2, args=("Thread 2",1, lock))
    print "Thread 1"
    our_thread_2 = threading.Thread (target = myfunction_1, args=("Thread 1",1, lock))
    print "Thread 2"
    our_thread_3 = threading.Thread (target = myfunction_3, args=("Thread 3",1, lock))
    print "Thread 3"
    our_thread_1.start()
    our_thread_2.start()
    our_thread_3.start()
# pass args to thread
    print "http://stackoverflow.com/questions/3221655/python-threading-string-arguments"
# loop in thread
    print "http://stackoverflow.com/questions/23100704/running-infinite-loops-using-threads-in-python"


if ( __name__ == "__main__" ):
    main()


