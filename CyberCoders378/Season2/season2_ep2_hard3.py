'''
This project is about finding the closest and easiest path between 2 point in a maze. The maze is a square field of
various values from 0 to 2. value of 1.0 and above are impassable, and values under 1 are gradient difficult to
traverse. 0 is open ground while 0.8 can be considered as hard mountain difficult to cross.

For ease of process the start is always (0, 0). and the destination is always the most bottom-right corner of the field.

You cannot go diagonally. You have to count the distance as manhattan_distance or taxicab distance.


The final answer to give as a length of the path.
'''

the_map = []
with open("map.txt") as file:
    for line in file:
        the_map.append([float(x) for x in line.strip().split()])
print(*the_map, sep="\n")