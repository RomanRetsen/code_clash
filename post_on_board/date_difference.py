'''
 Michel wants to know how many days there are between two dates. Please, help him find that number.
Use the Gregorian calendar.

- If the result is under 0 you need to return "error".
- If any date it's not valid, you need to return "Invalid Date"
Input
Line 1: The most recent date DATE1 (mm-dd-yyyy)
Line 2: The most oldest date DATE2 (mm-dd-yyyy)
Output
Line 1: A number of days



test 1

12-13-1989
12-21-1973

output
5836
---------------test2
03-25-2013
02-09-1989

output
8810

----------test3
26-02-2014
11-25-2016
output
Invalid Date
------------------test4

12-06-1986
10-29-2008

output

error
--------------test5


06-29-2008
10-24-1989

output
6823



'''

import datetime

try:
    recent = datetime.datetime.strptime(input(), '%m-%d-%Y')
    oldest = datetime.datetime.strptime(input(), '%m-%d-%Y')
    if recent < oldest:
        print("error")
    else:
        print((recent-oldest).days)
except ValueError :
    print("Invalid Date")
