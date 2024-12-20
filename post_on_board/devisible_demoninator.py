'''
You are given two sorted lists of positive integers, A and B.

Find all the integers, Z that are divisible by all integers in list A (Z mod A = 0) and also divide all integers in list B (B mod Z = 0).

If no intermediate factors exist, just print "None".
Input
Line 1: Two integers, sizeA and sizeB separated by a space, denoting the sizes of lists A and B.
Line 2: sizeA space separated integers in list A.
Line 3: sizeB space separated integers in list B.
Output
Line 1: A space separated list of integers that are evenly divisible by all integers in list A and evenly divide all integers in list B.
If no intermediate factors exist, just print "None".
Constraints
1 ≤ A, B < 2^31 - 1
1 ≤ sizeA, sizeB ≤ 10
---------------------------------test
10 10
91 92 93 94 95 96 97 98 99 100
1 2 3 4 5 6 7 8 9 10
output
None
---------------------------------test
1 3
3
6 9 12
output
3
---------------------------------test
2 2
2 3
24 48
output
6 12 24
---------------------------------test
3 2
3 5 6
30 90
output
30
---------------------------------test
1 1
1
100
output
1 2 4 5 10 20 25 50 100
---------------------------------test
1 3
3
30 45 99
output
3

---------------------------------test
1 3
2
50 1500 2147480000
output
2 10 50
---------------------------------test
---------------------------------test
---------------------------------test
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size_a, size_b = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
mm = max(a)
mx = min(b)
r = []
if mx < mm:
    print("None")
else:
    for i in range(mm, mx + 1, 1):
        if all((True if i % x == 0 else False for x in a)) and all((True if x % i == 0 else False for x in b)):
            r.append(i)

print(r)