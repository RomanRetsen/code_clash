'''
Given an integer n, find the next integer m with the same number of 1s in its binary expansion as n's.

For example, for n = 3 (dec) = 11 (bin), the next integer m with two 1s in its binary expansion is 101 (bin) = 5 (dec)
Input
The decimal representation of n
Output
The decimal representation of m
Constraints
0 < n < 1000

3
out
5
-----------------------
13
out
14

-------------------------
63
out
95
--------------------------
128
out
256
'''

import collections

n = int(input())
the_number = collections.Counter(bin(n))["1"]
print(the_number)
while not collections.Counter(bin(n + 1))["1"] == the_number:
    n += 1
else:
    print(n + 1)