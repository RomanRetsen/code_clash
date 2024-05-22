import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

from_num, end_num = input().split()
operator = input()

print(operator, " ".join([str(x) for x in range(int(from_num), int(end_num) + 1)]))
for i in range(int(from_num), int(end_num) + 1):
    # print(" ".join([f"{str(i)}{operator}{str(x)}" for x in range(int(from_num), int(end_num) + 1)]))
    print(str(i), " ".join([str(eval(f"{str(i)}{operator}{str(x)}")) for x in range(int(from_num), int(end_num) + 1)]))

