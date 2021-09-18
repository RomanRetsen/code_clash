"""
You are flying over enemy territory in a bomber. You have one bomb left and have to find the best spot to drop it.
Your bomb destroys everything in a 3x3 square. A square can either be an ally A or a target with score S represented by a single digit 0-9.
Your task is to find the x, y coordinates where the most damage can be inflicted, without hitting an ally (i.e. where the sum of scores is the highest in the 3x3 area around the coordinates).
Input
Line 1: the width W of the area
Line 2: the height H of the area
Next W lines: H characters either A or a digit 0-9.
Output
One line with the x and y coordinates.
0 0 is the top left.
W- 1 H- 1 is the bottom right.
Constraints
0 < W ≤ 16
0 < H ≤ 16
0 ≤ x < W
0 ≤ y < H

There always is a possible and only one best solution.
Example
Input

5
5
00000
01010
00300
01010
00000

Output

2 2


test2____________


5
4
00090
000A0
00550
05000

2 3

_______test3_____
16
16
0000000000000900
0003050000000000
0000000000000000
0000700000030000
0000010000000000
0001000000000002
0000000001000000
0000000000002000
0000000000000000
0004000000020000
0000000000000000
0400000200000000
0000000000090000
0000000060005000
0000080000200001
0000000000002000

11 13
----------------test4
6
5
101000
000AAA
010A09
000A09
000A09

5 3

____test5____________


7
7
AAA0000
A9A0000
AAA0000
0010100
0000000
0001000
0000000


3 4

_______test6_____________


7
5
A3AAAAA
AAAAAAA
A100AAA
A001AAA
A000AAA


2 3

"""

import itertools

def is_valid(a):
    if a[0] >= 0 and a[0] < height and a[1] >= 0 and a[1] < width:
        return True
    return False

coord = list(itertools.product([-1, 1, 0], repeat=2))
width = int(input())
height = int(input())
field = []

for i in range(height):
    field.append([x for x in input()])
damage = -100000
the_x = -1
the_y = -1
for x in range(height):
    for y in range(width):
        s = 0
        injure_aly = False
        for i in coord:
            if is_valid((x+i[0], y+i[1])):
                if field[x+i[0]][y+i[1]] == "A":
                    injure_aly = True
                    break
                else:
                    s += int(field[x+i[0]][y+i[1]])
        if s > damage and not injure_aly:
            damage = s
            the_x = y
            the_y = x

print(the_x, the_y)
