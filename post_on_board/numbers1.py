'''
Given an integer N, determine if there exist two integers a, b such that

a^2 - b^2 = N

Input
A single integer N.
Output
The answer: "they do" or "they don't"
Constraints
2 ≤ N ≤ 3,000
Example
Input

5

Output

they do
-----------------test2
2
output
they don't

-----------------test3
4
output
the do

---------------test4
1128
output
they do

-----------test5
1122
output
they don't

-----------test6
2003
output
they do

------------test7
2901
output
they do
'''

import itertools
import time

n = int(input())
t0 = time.time()
the_list = [x for x in range(n + 1) ]
# the_list = [x for x in range(math.floor(n ** 0.5) + 2)]
for i, y in itertools.combinations(the_list, r=2):
    if abs(i ** 2 - y ** 2) == n:
        print("they do")
        break
else:
    print("they don't")
print(f"My way took {time.time()-t0}")

t1 = time.time()
found = False
for i in range(n):
    for j in range(n):
        if (i+j)*(i-j) == n:
            print("they do")
            found = True
            break
    if found:
        break
else:
    print("they don't")
print(f"Other guy nested loop takes {time.time()-t1}")