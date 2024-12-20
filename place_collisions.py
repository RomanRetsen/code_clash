# You are in charge of monitoring an air space of dimensions W*H.
# You are given a list of coordinates (from the top-left corner) and directions representing the location and heading of an airplane at t=0 (first turn).
# At t=0, all the airplanes are inside your monitored space.
# They can only move in four directions, > ,v, < and ^.
# At each turn, all planes move simultaneously by exactly 1 unit in the direction they are headed.
# A collision is said to occur when two or more planes have the same coordinates at any given turn (however, the initial state is guaranteed to be collision free).
# A collision results in the immediate destruction of every plane involved.
#
# Write a program that will output the total number of collisions, in the air space you are monitoring.
#
# If required, you can visualize the different test cases interactively over there :
# https://xorzy.github.io/coc/airplane

# option 1
# 5
# 5
# 2
# 2 1 v
# 1 2 >
#
# result 1
# option 2
# 9
# 9
# 9
# 4 0 v
# 4 1 v
# 4 2 v
# 1 3 v
# 4 3 v
# 0 4 >
# 1 4 >
# 2 4 >
# 3 4 >

w = int(input())
h = int(input())
n = int(input())
planes = {}
collitions = 0
for i in range(n):
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    c = inputs[2]
    planes[i] = [x,y,c,'0']
print(planes)
while True:
    print(planes.items())
    for plane in planes.values():
        if plane[2] == '>':
            plane[0] +=1
        elif plane[2] == '<':
            plane[0] -= 1
        elif plane[2] == 'v':
            plane[1] += 1
        elif planes[2] == '^':
            plane[1] -= 1

    # for i in range(len(planes)):
    for plane_k, plane_value in planes.items():
        for in_k, in_v in planes.items():
            if in_k == plane_k:
                pass
            elif in_v[0] == plane_value[0] and in_v[1] == plane_value[1] and in_v[3] != 'x' and plane_value[3] != 'x':
                in_v[3] = 'x'
                plane_value[3] = 'x'
                collitions += 1
            elif in_v[0] == plane_value[0] and in_v[1] == plane_value[1] and in_v[3] != 'x' and plane_value[3] == 'x':
                in_v[3] = 'x'

    for i in (planes.keys()):
        if planes[i][3] == 'x' or \
            planes[i][0] > w or planes[i][0] < 0 or \
            planes[i][1] > h or planes[i][1] < 0:
            del planes[i]

    if not len(planes):
        break

print(int(collitions))