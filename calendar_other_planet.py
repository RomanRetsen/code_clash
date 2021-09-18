"""

On planet Calendor, 1 year lasts 11 months and 1 month lasts 17 days.

Months and days are named by their index: 1, 2, etc. The year can be negative or positive, but like on planet Earth, it can't be zero.

For some obscure reason, the months 7 and 10 have seven additional days.

You are given a date, and you should give the date of the next day.
Input
Y: the year (a non-zero integer).
M: the month (a number between 1 and 11).
D: the day (a number between 1 and 24).
Output
The year, the month and the day of the next day, separated by spaces.
Example
Input

2016 3 14

Output

2016 3 15



-----------test2

2001 5 17

2001 6 1



------------test3


-23 11 5

-23 11 6



__________test4

155 11 17

156 1 1


___-------test5

-78 11 17

-77 1 1

______________test6
-1 11 9

-1 11 10


------------test7
-1 10 24


-1 11 1


----------test8

8 10 17

8 10 18



"""

yy, m, d = [int(i) for i in input().split()]

if m == 7 or m == 10:
    x, y = divmod(d + 1, 24)
    if x == 1 and y == 1:
        m += 1
        d = y
    else:
        d += 1
    x, y = divmod(m, 11)
    if x == 1 and y == 1:
        yy += 1
        m = 1
else:
    x, y = divmod(d + 1, 17)
    if x == 1 and y == 1:
        m += 1
        d = y
    else:
        d += 1
    x, y = divmod(m, 11)
    if x == 1 and y == 1:
        yy += 1
        m = 1

print(yy, m, d)