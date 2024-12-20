"""
Consider a square a length of L where L is a multiple of 3

Consider the location of each element by (X, Y) where (0, 0) is the upper left cell.

Remove the four squares of length L/3 at extremities so that remaining part looks like a cross. and consider the remaining as the game board.

Example L = 9, X are the remaining items :

...XXX...
...XXX...
...XXX...
XXXXXXXXX
XXXXXXXXX
XXXXXXXXX
...XXX...
...XXX...
...XXX...



Now place a player at PX, PY on the board

From a list of moves expressed as a sequence of movements (U D R L), provide the final position of the player.

U means Up
D means Down
L means Left
R means Right

IMPORTANT NOTE :
- When the player reach the right or left limit of the board and move outside of the board ,he will respawn on the opposite cell at the same Y.
- When the player reach the top or bottom limit of the board and move outside of the board, he will respawn on the opposite cell at the same X.
Input
Line 1 :The length L of the board, it is a multiple of 3
Line 2 :The player x position pLocationX
Line 3 :The player y position pLocationY
Line 1 : A String moves composed with a list of chars :
- 'U' for Up
- 'D' for Down
- 'R' for Right
- 'L' for Left
Output
Line 1 :The final position (X Y) of the player
Constraints
Number of movements < 1000
L <= 300
Example
Input

9
3
3
R

Output

4 3

---------test2
9
3
3
RDLU

output
3 3
--------test3
9
3
1
RRR
output
3 1

----------test4
9
3
3
RUUUURRRULL
output
5 7
----------test5
300
110
123
UDUDDDRRRRRUDLRRRLRUDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURDLRLLUUUDLRDDDDDUUUUULLLLL
output
76 105
"""

import sys
import math

def make_move(p_x, p_y, move, l):
    limit_value = l // 3
    if move == "U":
        if p_x < limit_value or p_x >= 2 * limit_value:
            if p_y-1 < limit_value:
                p_y = 2 * limit_value - 1
            else:
                p_y -= 1
        else:
            if p_y - 1 < 0:
                p_y = l - 1
            else:
                p_y -= 1
    elif move == "D":
        if p_x < limit_value or p_x >= 2 * limit_value:
            if p_y+1 >= 2 * limit_value:
                p_y = limit_value
            else:
                p_y += 1
        else:
            if p_y + 1 >= l:
                p_y = 0
            else:
                p_y += 1
    elif move == "L":
        if p_y < limit_value or p_y >= 2 * limit_value:
            if p_x-1 < limit_value:
                p_x = 2 * limit_value - 1
            else:
                p_x -= 1
        else:
            if p_x - 1 <= 0:
                p_x = l-1
            else:
                p_x -= 1
    elif move == "R":
        if p_y < limit_value or p_y >= 2 * limit_value:
            if p_x+1 >= 2 * limit_value:
                p_x = limit_value
            else:
                p_x += 1
        else:
            if p_x + 1 >= l:
                p_x = 0
            else:
                p_x += 1
    return (p_x, p_y)

l = int(input())
p_location_x = int(input())
p_location_y = int(input())
correction_x = 0
correction_y = 0
for move in input():
    p_location_x, p_location_y = make_move(p_location_x, p_location_y, move, l)

print(p_location_x, p_location_y)
