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
import heapq
import time

class Graph:
    def __init__(self):
        self.edge_data = {}
        self.vertex_data = {}

    def add_edge(self, s_x, s_y, d_x, d_y, weight):
        self.edge_data[(s_x, s_y, d_x, d_y)] = weight

    def add_vertex_data(self, x, y):
        self.vertex_data[(x, y)] = [False, None, math.inf, []]


def load_map(file):
    the_map = []
    with open(file) as file:
        for line in file:
            the_map.append([float(x) for x in line.strip().split()])
    print(*the_map, sep="\n")
    return the_map

def generate_graph(the_map):
    the_l = len(the_map)
    the_graph = Graph()

    # fill dictionary with all viable vertcies data
    for i in range(the_l):
        for y in range(the_l):
            if the_map[i][y] < 1:
                the_graph.add_vertex_data(i, y)
    the_graph.vertex_data[(0,0)][2] = 0

    # add edge/links values and neighbours
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
    return the_graph


def find_path_v1_list(the_graph):
    unchecked_vertex = [x for x in the_graph.vertex_data]
    while len(unchecked_vertex):
        current = min(unchecked_vertex, key=lambda x:the_graph.vertex_data[x][2])
        the_graph.vertex_data[current][0] = True
        for neighbour in the_graph.vertex_data[current][3]:
            if the_graph.vertex_data[neighbour][0] == True:
                continue
            new_distance = the_graph.vertex_data[current][2] + the_graph.edge_data[current + neighbour]
            if new_distance < the_graph.vertex_data[neighbour][2]:
                the_graph.vertex_data[neighbour][2] = new_distance
                the_graph.vertex_data[neighbour][1] = current
        unchecked_vertex.clear()
        unchecked_vertex = [x for x in the_graph.vertex_data if not the_graph.vertex_data[x][0]]

# for some home using heap takes longer time
def find_path_v2_heap(the_graph):
    unchecked_vertex = [(the_graph.vertex_data[x][2],index, x) for index,x in enumerate(the_graph.vertex_data)]
    heapq.heapify(unchecked_vertex)
    while len(unchecked_vertex):
        current = heapq.heappop(unchecked_vertex)[2]
        the_graph.vertex_data[current][0] = True
        for neighbour in the_graph.vertex_data[current][3]:
            if the_graph.vertex_data[neighbour][0] == True:
                continue
            new_distance = the_graph.vertex_data[current][2] + the_graph.edge_data[current + neighbour]
            if new_distance < the_graph.vertex_data[neighbour][2]:
                the_graph.vertex_data[neighbour][2] = new_distance
                the_graph.vertex_data[neighbour][1] = current
        heapq.heapify(unchecked_vertex)

def print_graph(the_graph):
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

# BACKTRACKING
def is_valid_step(x, y, the_map, l_map):
    if 0 <= x < l_map and 0 <= y < l_map and the_map[x][y] < 1:
        return True
    return False

def find_path_backtracking(x, y, the_map, l_map, )


if __name__ == "__main__":
    the_map = load_map("map.txt")
    # using Dijkstra
    t1 = time.time()
    the_graph = generate_graph(the_map)
    find_path_v1_list(the_graph)
    t0 = time.time()
    print(f"Time needed to find path{t1-t0}")
    print(the_graph.vertex_data[(99, 99)])
    print_graph(the_graph)
    # using backtracking





















