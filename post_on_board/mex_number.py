"""
MEX stands for minimum excluded. Given a list of integers return the lowest non-negative integer that is not present in the list otherwise known as MEX of the list.
Input
Line 1: n, the number of integers in the list
Line 2: n integers ai, separated with a space
Output
MEX - the lowest non-negative integer that is not present in the array
Constraints
1 <= n <= 100
0 <= ai <= 100
Example
Input

5
1 2 3 0 5

Output

4
---------test2
5
3 4 2 7 5

output

0
-----------test3
100
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99

output
100
----------test4
2
1 2

ouput
0
"""

the_list = []
n = int(input())
for i in input().split():
    x = int(i)
    if x >= 0:
        the_list.append(x)
mx = max(the_list)
print(min(set(range(0, mx+2, 1)) - set(the_list)))

