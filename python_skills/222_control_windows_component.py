#!/usr/bin/python
#-*- coding:utf-8 -*-

import win32com, os


word = win32com.client.Dispatch("Word.Application")

# run in background not alert
word.Visible = 0
word.DisplaAlerts = 0

# Open new file
doc = word.Documents.Open( FileName = "new_word.doc")

# insert words
myRange = doc.Range(0,0)
myRange.InsertBefore("Hello from Python!")

# use style
wordSel = myRange.Select()
wordSel.Style = constants.wdStyleHeading1

# print 
doc.PrintOut()

# close
word.Document.Close(wc.wdDoNotSaveChanges)
word.Quit()

os.system("pause")
