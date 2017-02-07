#!/usr/bin/python
#-*- coding:utf-8 -*-

from datetime import timedelta as td
a = td(days=2, hours=6)
print(a)
b = td(hours=4.5)
print('a + b', a + b)
c = a + b
print('c.days : ', c.days)
print('c.seconds:',c.seconds)
print('c.seconds / 3600', c.seconds / 3600)
print('c.total_seconds() / 3600', c.total_seconds() / 3600)

from datetime import datetime
a = datetime(2012,9,23)
print('a + td(days=10)',a + td(days=10))

now = datetime.today()
print('now',now)
print('now + td(minutes=10)',now + td(minutes=10))

a = datetime(2012,3,1)
b = datetime(2017,2,7)
print('a - b', a - b)
print('(a - b).days', (a - b).days)


from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))

d = relativedelta(a,b)
print('relative delta about a and b:', d)
print('(b - a) months', d.months)
print('(b - a) days', d.days)
