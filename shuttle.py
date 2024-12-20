import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
target_x = -1
target_y = -1
previous_x = -1
previous_y = -1
target_width = 0


for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if land_y == previous_y and land_x - previous_x - 1000 >= target_width - 1000 :
        target_x = previous_x
        target_y = previous_y
        target_width = land_x - previous_x

    previous_x = land_x
    previous_y = land_y
print(f'{target_x} {target_y}')