#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 077_parse_csv_file.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-25 22:09:00
#Last Modifieda: 2016-09-25 22:09:00
#*********************************************************

import csv
with open('./addon/Windows-8-stats.csv') as csvfile:
    with open('./addon/New-Window-8-stats.csv',"wb") as w_csvfile:
        inforeader = csv.reader(csvfile, delimiter=",")
        infowriter = csv.writer(w_csvfile,delimiter="!")
        for row in inforeader:
            print "!".join(row)
            infowriter.writerow(row)


