#!/usr/bin/python
#-*- coding:utf-8 -*-


# 1.15 Grouping Records Together based on a Field


rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


from operator  import itemgetter
from itertools import groupby



# Sort by the desired filed first
rows.sort(key = itemgetter('date'))


for item in groupby(rows, key = itemgetter('date')):
    print(item)
# Iterate in groups
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for item in items:
        print(' ', item)

print("\n\n\nUse collections defaultdict")
from collections import defaultdict
row_by_date = defaultdict(list)
for row in rows:
    row_by_date[row['date']].append(row)

for date in row_by_date.keys():
    print(date)
    for row in row_by_date[date]:
        print(row)
