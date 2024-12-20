"""
Amicable numbers are two numbers such as the sum of the proper divisors of each is equal to the other number.
For example 220 and 284 are amicable because:
sum(divisors(220)) = 1+2+4+5+10+11+20+22+44+55+110 = 284
sum(divisors(284)) = 1+2+4+71+142 = 220

Providing a list of integers you need to write a script that outputs their amicable numbers if any.
Input
Line 1 : N the number of numbers to test
Line 1 : A space-separated list L of N integers
Output
N lines For each integer in L print its related amicable number if any, else print -1
Constraints
1 ≤ N ≤ 1000
Example
Input

3
1 220 440

Output

-1
284
-1
----------------test2
5
1562 2620 3562 2923 4568


-1
2924
-1
-1
-1
-------------------------
"""


def sum_of_divisors(n):
    r = []
    for i in range(1, n):
        if n % i == 0:
            r.append(i)
    return 1 if len(r) == 0 else sum(r)
n = int(input())
for i in (int(x) for x in input().split()):
    t = sum_of_divisors(i)
    t2 = sum_of_divisors(t)
    if t == t2:
        print(t2)
    else:
        print(-1)


