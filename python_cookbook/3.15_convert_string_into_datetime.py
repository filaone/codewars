#!/usr/bin/python
#-*- coding:utf-8 -*-


from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
diff = z - y
print('diff = z - y', diff)


nice_z = datetime.strftime(z, "%A %B %d, %Y")
print('nice_z', nice_z)
