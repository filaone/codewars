#!/usr/bin/python
#-*- coding:utf-8 -*-

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_bydays(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = datetime.weekday(start_date)
    dat_num_target = weekdays.index(dayname)
    days_ago = (day_num - dat_num_target + 7) % 7
    if days_ago == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


print('get_previous_bydays("Monday")', get_previous_bydays('Monday'))
print('datetime', get_previous_bydays('Sunday', datetime(2012,12,21)))

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# Next Friday
print("d + relativedelta(weekday=FR)", d + relativedelta(weekday=FR))
# Last Friday
print("d + relativedelta(weekday=FR(-1))", d + relativedelta(weekday=FR(-1)))
