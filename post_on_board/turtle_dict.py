'''
A turtle moves on a board by following a sequence of simple instructions :
LEFT to turn left
RIGHT to turn right
or an integer d indicating the distance to be covered (note that d can be negative when the turtle has to move backwards)

The turtle is initially aligned on the horizontal axis looking to the right.
Input
Line 1: 2 integers x and y for the coordinates of the starting point
Line 2: An integer n for the number of instructions given to the turtle
n next lines: cmd containing either a LEFT or RIGHT instruction or a distance to travel
Output
A line containing x and y the new coordinates of the turtle.
Constraints
0<n<100
-100<=x,y,distance<=100
Example
Input

50 50
3
10
RIGHT
10

Output

60 40
--------------test2
0 0
2
10
-30
output
-20 0
--------------test3
0 0
9
10
RIGHT
10
LEFT
10
RIGHT
10
LEFT
10
output
30 -20
-----------test4
0 0
8
10
LEFT
10
LEFT
10
LEFT
10
LEFT
output
0 0

----------test
0 0
13
8
LEFT
30
LEFT
-10
LEFT
61
RIGHT
39
-6
LEFT
LEFT
12
output
-3 -31
'''

current_direction = "E"
turtle_direction = {"E":{"L":"N", "R":"S"}, "W":{"L":"S", "R":"N"},"N":{"L":"W", "R":"E"},"S":{"L":"E", "R":"W"},}
direction_vector = {"E":1, "W":-1,"N":1,"S":-1}
current_vector = 1

x,y = [int(x) for x in input().split()]
n = int(input())
for i in range(n):
    distance_or_turn = input()
    if distance_or_turn in ["RIGHT", "LEFT"]:
        current_direction = turtle_direction[current_direction][distance_or_turn[0]]
        current_vector = direction_vector[current_direction]
    else:
        distance = int(distance_or_turn)
        if current_direction in ["W", "E"]:
            x += distance * current_vector
        elif current_direction in ["N", "S"]:
            y += distance * current_vector
print(x,y)

'''
solution from Germany :))

x, y = [int(i) for i in input().split()]
n = int(input())
dist = 0
orientation = 0
print(f'{x=} {y=}', file=sys.stderr, flush=True)
for i in range(n):
    cmd = input()

    if cmd == 'LEFT':
        orientation = (orientation + 1)%4
    elif cmd == 'RIGHT':
        orientation = (orientation - 1)%4
    else:
        dist = int(cmd)
        if orientation == 0:
            x += dist
        elif orientation == 1:
            y += dist
        elif orientation == 2:
            x -= dist
        elif orientation == 3:
            y -= dist

print(x,y)
'''















