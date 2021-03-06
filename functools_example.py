"""
You will receive an integer n, an array of size N of perceptron inputs [x1, x2, ..., xn], an array of size N + 1 of perceptron weights [w0, w1, ..., wn] and must output y, the result of the step activation function.

step(u) = 0 if u <= 0
step(u) = 1 otherwise

u = -w0 + w1 * x1 + ... + wn * xn
y = step(u)
Input
Line 1: An integer N
Line 2: N space separated integers x1 x2 ... xn
Line 3: N+1 space separated integers w0 w1 ... wn
Output
An integer y
Constraints
2 ≤ N ≤ 100
-1 ≤ xi ≤ 1
-1 ≤ wi ≤ 1
Example
Input

2
-0.85 -0.29
-0.04 -0.75 -0.89

Output

1


---------------test 2

3
0.35 -0.41 0.42
0.25 -0.14 0.98 -0.94

0

----------test 3
4
-0.68 -0.14 -0.65 -0.47
0.42 0.37 -0.45 0.72 -0.50

0

-----------test4

100
0.07 -0.72 -0.18 0.73 0.61 -0.46 0.43 -0.73 -0.38 -0.50 0.36 0.63 0.98 0.35 0.16 0.96 0.48 -0.44 -0.68 -0.73 0.46 -0.25 0.03 0.56 0.02 -0.25 -0.84 0.63 0.02 -0.44 -0.48 -0.17 0.56 -0.43 0.92 -0.45 0.19 -0.70 -0.70 -0.76 0.56 0.56 0.66 0.85 -0.20 0.87 -0.23 0.56 0.43 0.44 0.63 0.02 0.62 -0.63 -0.50 0.97 -0.24 -0.28 0.08 0.30 0.51 0.93 -0.73 -0.48 -0.65 0.50 0.69 -0.52 -0.35 -0.30 -0.95 -0.32 -0.98 -0.50 0.67 0.13 0.43 0.76 -0.04 -0.67 0.31 0.58 0.03 0.20 -0.47 0.48 -0.48 -0.06 0.28 -0.95 0.72 0.73 -0.25 -0.97 0.45 -0.22 0.12 -0.83 -0.03 -0.88
0.50 -0.29 -0.05 0.24 -0.36 0.92 -0.07 0.43 0.39 -0.69 0.59 -0.21 -0.38 -0.07 -0.89 0.33 0.85 0.27 0.41 -0.78 -1.00 -0.53 0.34 0.90 -0.57 0.80 -0.34 0.53 -0.41 -0.22 0.16 -0.48 0.86 0.17 0.22 0.86 -0.14 0.15 0.46 -0.42 -0.99 0.09 -0.74 0.43 0.40 -0.95 0.10 -0.87 0.92 0.20 0.11 0.08 -0.25 0.83 0.21 0.81 -0.46 0.69 0.19 -0.17 0.20 0.43 0.68 0.15 -0.60 -0.82 0.36 0.92 0.94 0.04 0.21 -0.60 0.79 -0.83 -0.24 0.95 -0.66 0.36 0.50 0.80 -0.80 0.64 0.00 0.57 0.16 0.44 -0.63 0.36 0.93 0.08 -0.78 0.37 0.26 -0.21 -0.16 0.80 0.40 -0.05 -0.43 -0.59 -0.88


1

-----------------------------
"""

#power of reduce function

import functools

n = int(input())
perceptrons = [float(x) for x in input().split()]
weights = [float(x) for x in input().split()]

r = functools.reduce(lambda x,y:(x + y[0]*y[1]), zip(perceptrons, weights[1:]), -1 * weights[0])

print("0") if r <= 0 else print("1")