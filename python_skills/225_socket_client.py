#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket, os

HOST = "127.0.0.1"
PORT = 8888

# getaddrinfo return a list of 5-tuples
# (family, socktype, proto, canonname, sockaddr)
for res in socket.getaddrinfo(HOST, PORT):
    family,socktype,proto,canonname,sockaddr = res
    try:
	    s = socket.socket(famil,socktype,proto)
	except socket.error, msg:
	    s = None
		continue
	try:
	    s.connect(sockaddr)
	except socket.error, msg:
	    s.close()
		s = None
		continue
	break
if s is None:
    print 'Could not open Socket'
	sys.exit(1)

s.sendall("Hello World!")
data = s.recv(1024)
s.close()
print "Received : ", repr(data)
end = raw_input("END")

