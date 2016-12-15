#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 207_parse_args.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-04 22:18:34
#Last Modifieda: 2016-12-04 22:18:34
#*********************************************************

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers',metavar='N', type=int, nargs='+',
                    help='an integer for the accmulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print args.accumulate(args.integers)
print "hello"
