"""
Your task is to sum all values in a square above the diagonal running from the top left corner of the square to the bottom right corner.

Example: The size of square is 4.
Values in square are:
1 2 3 4
5 6 7 8
1 2 3 9
5 6 7 8

The numbers above the diagonal are: 2, 3, 4, 7, 8, 9.
The sum of these numbers is 2+3+4+7+8+9 = 33.
So the output is 33.
Input
N - determine size of square
then are the numbers in square
Output
The sum of all values above the diagonal from right to left
Constraints
0<N<10
Example
Input

4
1
2
3
4
5
6
7
8
1
2
3
9
5
6
7
8

Output

33

--------------------test 2
3
12
16
8
4
12
2
5
8
21

out
26
---------------test 3
5
2
6
18
21
44
7
18
92
16
14
13
12
8
0
2
3
3
2
16
75
27
48
82
1
64

out
288
---------------test4
4
-112
-342
-661
192
99
1789
-164
-111
461
671
-99
101
61
124
-21
999

out
-985
"""
n = int(input())
s = 0
for i in range(n):
    for j in range(n):
        value = int(input())
        if j > i:
            s += value

print(s)



