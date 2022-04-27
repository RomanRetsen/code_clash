import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

a = b = 1
d = 10000000
increase = True

while True:
    print(f"Trying new distance {n-b}")
    if ((new_d := abs(n-b)) < d) and (abs(n-b) >= 0):
        d = new_d
    else:
        break
    a, b = b, a+b
print(d)