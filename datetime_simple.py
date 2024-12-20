import datetime
import string





n = int(input())
for i in range(n):
    b, d = input().split(" ")
    b_date = datetime.datetime.strptime(b, "%m/%d/%Y")
    d_date = datetime.datetime.strptime(d, "%m/%d/%Y")
    if d_date.month > b_date.month:
        print(d_date.year - b_date.year)
    elif d_date.month == b_date.month and d_date.day >= b_date.day:
        print(d_date.year - b_date.year)
    elif d_date.month == b_date.month and d_date.day < b_date.day:
        print(d_date.year - b_date.year - 1)
    elif d_date.month < b_date.month:
        print(d_date.year - b_date.year - 1)


"""
#adding 1 month to a date
from dateutil.relativedelta import relativedelta
import datetime


m = int(input())
y = int(input())

test_date = datetime.datetime(year=y, month=m, day=1)
next_first = test_date + relativedelta(months=1)
print((next_first - test_date).days)
"""