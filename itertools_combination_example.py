from itertools import combinations
import math

n = int(input())

range_number = int(math.pow(n,(1/3)))
all_pos = [x ** 3 for x in range(1, range_number + 1)]
print(all_pos)
counter = 0
# print([list(combinations(all_pos, x)) for x in range(1, len(all_pos) + 1)])
print(len([sum(x) for y in range(1, len(all_pos) + 1) for x in combinations(all_pos, y) if sum(x) == n]))


# Check if a number is a sum of distinct positive numbers' cubes.
# You have to tell how many possibles solutions.
#
# Example : 9 = 1³ + 2³
# (1,2) and (2,1) are the the same answer and count only once.
#
# Note that we only consider here sums with at least two operands.
# Input
# Integer N
# Output
# Integer R
# Constraints
# N < 10000
# Example
# Input
#
# 9
#
# Output
#
# 1
#
# 1729
#
# 4
#
#
# _______
#
# 8890
#
# 15
#
#