#!/usr/bin/python
#-*- coding:utf-8 -*-

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encounterd a start tag : ", tag
    def handle_endtag(self, tag):
        print "Encounterd an end  tag : ", tag
    def handle_data(self, data):
        print "Encounterd some data : ", data

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')

