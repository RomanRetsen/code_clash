import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, n = [int(i) for i in input().split()]
f1 = lambda x:l//2+x if l%2 == 0 else l//2-x
f2 = lambda x:l//2-1-x if l%2 == 0 else l//2+1+x
my_list = [f(x) for x in range(l//2 + 1) for f in (f1,f2) if f(x) < l]
# my_list = [x for x in range(l) ]
#
print(my_list.index(n))
# print(my_list)
# for i in range(l-1):
#     my_list = my_list[-1-i::-1] + my_list[l-i:]
#     print(my_list)
#     new_index = my_list.index(n)
#     print(f'new index {new_index}')
# print(my_list)
#
# 0 1 2 3 4
#
# We have to track down the element "3". We transform the sequence by the rule:
#
# (1) On round 1, the entire sequence is reversed:
#
# 0 1 2 3 4 -> 4 3 2 1 0
#
#
# (2) On round 2, the last 1 element remains still, while the rest being reversed:
#
# 4 3 2 1 0 -> 1 2 3 4 0
#
#
# (3) On round 3, the last 2 elements remain still, while the rest being reversed:
#
# 1 2 3 4 0 -> 3 2 1 4 0
#
#
# (4) On round 4, the last 3 elements remain still, while the rest being reversed:
#
# 3 2 1 4 0 -> 2 3 1 4 0
#
#
# We can see the element "3" has an index of 1 in the final sequence, thus the output should be 1.
#
# Hint: The length of the sequence can get REALLY LARGE in some test cases. Watch out for a timeout!
#
# 804180 71203
# 661773
#
# 100 76
# 52