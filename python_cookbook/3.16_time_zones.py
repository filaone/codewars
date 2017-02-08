#!/usr/bin/python
#-*- coding:utf-8 -*-

from datetime import datetime
from pytz import timezone

d = datetime.now()
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
