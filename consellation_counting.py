import math


def dist(input_a, input_b):
    return math.sqrt( (input_a[0] - input_b[0])** 2 + (input_a[1] - input_b[1]) ** 2)

h, w, distance_threshhold = map(int, input().split())
sky = []
for i in range(h):
    sky.append([[x, i, index, False] for index, x in enumerate(input())])
consellations_number = 0
consellations_stack = []
new_addition_stack = []
loop_through_stack = []
print(f'sky before {sky}')
for i in range(h):
    for y in range(w):
        print(sky[i][y])
        if sky[i][y][3] == False and sky[i][y][0] == "*":
            sky[i][y][3] = True
            # start_point = sky[i][y]
            consellations_stack.clear()
            new_addition_stack.clear()
            consellations_number += 1
            consellations_stack.append(sky[i][y])
            new_addition_stack.append(sky[i][y])
            need_converging = True
            while need_converging:
                need_converging = False
                consellations_stack.extend(new_addition_stack)
                loop_through_stack = new_addition_stack[:]
                new_addition_stack.clear()
                for start_point in loop_through_stack:
                    print(f'loop_through_stack {loop_through_stack}')
                    # print(need_converging, start_point, '--', consellations_stack)
                    for ii in range(i, h):
                        for yy in range(0, w):
                            # print(f'ii {ii}; yy {yy}')
                            if distance_threshhold >= dist(tuple(sky[ii][yy][1:3]), tuple(start_point[1:3])) and \
                                    sky[ii][yy][0] == '*' and sky[ii][yy] not in consellations_stack and \
                                    sky[ii][yy] not in new_addition_stack:
                                # print(sky[ii][yy][1:3], start_point[1:3])
                                sky[ii][yy][3] = True
                                new_addition_stack.append(sky[ii][yy])
                                need_converging = True
        else:
            pass


print(f'sky after {sky}')
print(consellations_number)



# Beginner astrophotographer Oleg took a photo of the night sky. Now he wants to find a number of constellations in it. This photo is h pixels in height and w pixels in width and each pixel is either a star (*) or an empty region (.). A star can be described by its coordinates (x, y) in the photo. He found following algorithm to identify constellations:
#
# 0) Initially, each star is considered as a separate constellation
# 1) Choose two stars in different constellations. Let (x1, y1) and (x2, y2) be coordinates of those stars.
# 2) If the rectilinear distance between stars is under given threshold t, i.e. |x1 - x2|+|y1 - y2|≤ t, then merge corresponding constellations.
# 3) Repeat steps #1-2 until no merging occurs
#
# Oleg asks you to implement above algorithm and count constellations in the photo.
# Input
# Line 1: Three space-separated integers h (height of the photo), w (width of the photo), t (distance threshold)
# Next h lines: String representing a row of the photo. It consists of characters . (empty region) and * (star)
# Output
# Print a number of constellations in the photo
# Constraints
# 1 ≤ h, w < 100
# 1 ≤ t < 200
# Number of stars is guaranteed to be less than or equal to 256.
# 4 5 1
# *....
# *....
# ....*
# ...**
#
# 4 5 1
# **...
# *....
# *...*
# ...**
#
# 4 5 1
# **...
# *....
# ....*
# ...**
#
# 2
#
# _____________
#
# 3 3 3
# ...
# ...
# ...
#
# 0
#
#
# _________________
#
# 22 22 1
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
# *.*.*.*.*.*.*.*.*.*.*.
# .*.*.*.*.*.*.*.*.*.*.*
#
# 242
#
# _____
# 1 1 1
# *
#
# 1
# 16 16 1
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
#
# 1
#
#
#
#
# 5 16 1
# ****************
# ****************
# ****************
# ****************
# ****************
#
# 1