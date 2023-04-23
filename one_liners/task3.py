'''
You will be given a starting number start and a closing number end. You must find the number of numbers in between start and end (both inclusive) that apply to the following condition:
⇨ The sum of its digits should be greater than or equal to the product of its digits.

For Example: If start = 50 and end = 60, there are three numbers that apply to the condition.
They are 50 ( product = 0, sum = 5 ), 51 ( product = 5, sum = 6 ) and 60 ( product = 0, sum = 6 )
Input
Line1: [start] and [end]
Output
Line 1: No. of magic numbers
Constraints
10 < start < end < 5000
Example
Input

20 30

Output

4

--------------test2

input
200 366
output
43
------------test3
input
560 561
output
1
-----------test4
input
11 4999
output
1373

'''

start, end = [int(i) for i in input().split()]
s = lambda x:sum([int(i) for i in x])
p = lambda x:eval("*".join([i for i in x]))

r = [x for x in range(start, end + 1) if s(str(x)) >= p(str(x))]
print(len(r))
