#!/usr/bin/python 
#-*- coding:utf-8 -*-

print "Threads are used for small tasks, whereas processes are used for 'heavyweight' tasks - basically the execution of application. Another different between a thread and a process is that threads within the same process share the same address space, whereas different processes do not."

print "The threading module uses threads, the multiprocess uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. That is what the global  interpreter lock is for."

print "Spawning processes is a bit slower than spawning  threads. Once they are running, there is not much difference."

