"""
---------------------------------------
Return the output of the Ackermann function.

If at least one of the numbers given is negative, return -1.

Ackermann function:
if M = 0: return n + 1
if N = 0: return Ackermann function of M - 1, 1
Default: return Ackermann function of (M - 1, Ackermann function of(M, N - 1))
Input
The variables M and N
Output
The output of the Ackermann function
Constraints
-1 ≤ M < 3
-1 ≤ N ≤ 100
Example


-------------test1
Input

0 99

Output

100

-----------test2
1 0

2

-------------test3

-1 5

-1

-----------test4
2 55

113

----------test5

2 97

197

"""
import sys

counter = 0
def acerman_func(m ,n):
    global counter
    counter += 1
    if m < 0:
        return -1
    elif m == 0:
        return n + 1
    elif n == 0:
        return acerman_func(m-1, 1)
    else:
        return acerman_func(m -1, acerman_func(m, n-1))

m, n = [int(i) for i in input().split()]

def acerman_loop(m, n):
    if m < 0:
        return -1
    elif m == 0:
        return n + 1
    elif n == 0:
        temp_val = 0
        while m > 0:
            acerman_func(m-1, 1)
        return temp_val
    else:
        return acerman_func(m -1, acerman_func(m, n-1))

#using recursion but recursion has depth limit
print(f'recursion limit is  {sys.getrecursionlimit()}')
print(acerman_func(m, n))
print(f'counter {counter}')
#using loops
# print(acerman_loop(m, n))
