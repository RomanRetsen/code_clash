'''
This project is about finding the closest and easiest path between 2 point in a maze. The maze is a square field of
various values from 0 to 2. value of 1.0 and above are impassable, and values under 1 are gradient difficult to
traverse. 0 is open ground while 0.8 can be considered as hard mountain difficult to cross.

For ease of process the start is always (0, 0). and the destination is always the most bottom-right corner of the field.

You cannot go diagonally. You have to count the distance as manhattan_distance or taxicab distance.


The final answer to give as a length of the path.
'''
import numpy as np
import matplotlib.pyplot as plt
import math


the_map = []
with open("map.txt") as file:
    for line in file:
        the_map.append([float(x) for x in line.strip().split()])
print(*the_map, sep="\n")
the_l = len(the_map)

class Graph:
    def __init__(self, size):
        self.edge_data = {}
        self.size = size
        self.vertex_data = {}

    def add_edge(self, s_x, s_y, d_x, d_y, weight):
        self.edge_data[(s_x, s_y, d_x, d_y)] = weight

    def add_vertex_data(self, x, y):
        self.vertex_data[(i, y)] = [False, None, math.inf, []]


the_graph = Graph(the_l * the_l)

for i in range(the_l):
    for y in range(the_l):
        if the_map[i][y] < 1:
            the_graph.add_vertex_data(i, y)

the_graph.vertex_data[(0,0)][2] = 0


for vertex in the_graph.vertex_data:
    if (vertex[0]-1, vertex[1]) in  the_graph.vertex_data:
        the_graph.add_edge(vertex[0], vertex[1], vertex[0]-1, vertex[1], the_map[vertex[0]-1][vertex[1]])
        the_graph.vertex_data[vertex][3].append((vertex[0]-1, vertex[1]))
    if (vertex[0], vertex[1]-1) in  the_graph.vertex_data:
        the_graph.add_edge(vertex[0], vertex[1], vertex[0], vertex[1]-1, the_map[vertex[0]][vertex[1]-1])
        the_graph.vertex_data[vertex][3].append((vertex[0], vertex[1]-1))
    if (vertex[0]+1, vertex[1]) in  the_graph.vertex_data:
        the_graph.add_edge(vertex[0], vertex[1], vertex[0]+1, vertex[1], the_map[vertex[0]+1][vertex[1]])
        the_graph.vertex_data[vertex][3].append((vertex[0] + 1, vertex[1]))
    if (vertex[0], vertex[1]+1) in  the_graph.vertex_data:
        the_graph.add_edge(vertex[0], vertex[1], vertex[0], vertex[1]+1, the_map[vertex[0]][vertex[1]+1])
        the_graph.vertex_data[vertex][3].append((vertex[0], vertex[1]+1))


# print(len([x for x in the_graph.vertex_data if not the_graph.vertex_data[x][0]]))
# print(max([x for x in the_graph.vertex_data if the_graph.vertex_data[x][0]], key=lambda x:the_graph.vertex_data[x][2]))
unchecked_vertex = [x for x in the_graph.vertex_data]
while len(unchecked_vertex):
    current = min(unchecked_vertex, key=lambda x:the_graph.vertex_data[x][2])
    the_graph.vertex_data[current][0] = True
    # print(the_graph.vertex_data[current])
    for neighbour in the_graph.vertex_data[current][3]:
        # print(neighbour)
        if the_graph.vertex_data[neighbour][0] == True:
            continue
        new_distance = the_graph.vertex_data[current][2] + the_graph.edge_data[current + neighbour]
        if new_distance < the_graph.vertex_data[neighbour][2]:
            the_graph.vertex_data[neighbour][2] = new_distance
            the_graph.vertex_data[neighbour][1] = current
        # print(the_graph.vertex_data[neighbour])
    unchecked_vertex.clear()
    unchecked_vertex = [x for x in the_graph.vertex_data if not the_graph.vertex_data[x][0]]

print(the_graph.vertex_data[(99, 99)])

end = (99,99)
the_map[99][99] = -1
while not (path_element := the_graph.vertex_data[end][1]) == (0,0):
    the_map[path_element[0]][path_element[1]] = -1
    end = path_element
else:
    the_map[0][0] = -1

H = np.array(the_map)
plt.imshow(H, interpolation='none')
plt.show()
