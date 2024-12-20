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
from time import time
import sys
from collections import namedtuple

class Graph:
    def __init__(self):
        self.edge_data = {}
        self.vertex_data = {}

    def add_edge(self, s_x, s_y, d_x, d_y, weight):
        self.edge_data[(s_x, s_y, d_x, d_y)] = weight

    def add_vertex_data(self, x, y):
        self.vertex_data[(x, y)] = [False, None, math.inf, []]


def load_map(file):
    # the_map = [[0 for _ in range(38)] for _ in range(38)]
    the_map = []
    with open(file) as file:
        for line in file:
            the_map.append([float(x) for x in line.strip().split()])
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
all_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
all_direction2 = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class BestPath:
    def __init__(self, value, bestpath):
        self.value = value
        self.bestpath = bestpath

def is_valid_step(x, y, the_map, l_map):
    if 0 <= x < l_map and 0 <= y < l_map and the_map[x][y] < 1 and the_map[x][y] < 1:
        return True
    return False

def calculate_path_value(the_map, the_path):
    the_total = 0
    for step in the_path:
        the_total += the_map[step[0]][step[1]]
    return the_total


def find_path_backtracking(x, y, l_map, the_map, solution_map, the_path, current_path, level, reset, best_path):
    if x == l_map-1 and y == l_map-1 and reset:
        the_path.append(current_path)
        print(f"the_path : {the_path}")
        calc_value = calculate_path_value(the_map, the_path)
        print(f"This path value is {calc_value}; BUT current best is {best_path.value}")
        if best_path.value > calc_value:
            best_path.value = calc_value
            best_path.bestpath = the_path[:]
        del the_path[-1]
        the_path.append((-1, -1))
        return False
    if is_valid_step(x, y, the_map, l_map):
        # print(f"I'm am at {(x,y)} on level {level}")
        if solution_map[x][y] == 1 or calculate_path_value(the_map, the_path) >= best_path.value:
            # print(f"Have to false out at {x}-{y}")
            return False
        if solution_map[x][y] == 2 and not reset:
            # print(f"2 and reset is False at {x}-{y}")
            return False
        # if solution_map[x][y] == 2 and reset:
        #     print(f"2 and reset is True at {x}-{y}")
            # return Fals

        if solution_map[x][y] == 0:
            reset = True
        solution_map[x][y] = 1
        if (x,y) in the_path:
            input("double")
        the_path.append((x,y))
        if x >= y:
            for direction in all_direction2:
                current_path = (x + direction[0], y + direction[1])
                if find_path_backtracking(x + direction[0], y + direction[1], l_map, the_map, \
                                       solution_map, the_path, current_path, level+1, reset, best_path):
                    return True
                if the_path[-1] == (-1,-1):
                    reset = False
                    del the_path[-1]
        else:
            for direction in all_direction:
                current_path = (x + direction[0], y + direction[1])
                if find_path_backtracking(x + direction[0], y + direction[1], l_map, the_map, \
                                          solution_map, the_path, current_path, level + 1, reset, best_path):
                    return True
                if the_path[-1] == (-1, -1):
                    reset = False
                    del the_path[-1]
        solution_map[x][y] = 2
        del the_path[-1]
        return False
    return False

def display_steps(l_map, solution_matrix, the_path):
    solution_matrix_copy = solution_matrix[:]
    for number, step in enumerate(the_path, 10):
        solution_matrix_copy[step[0]][step[1]] = number
    for i in range(l_map):
        print(*[f"{solution_matrix_copy[i][x]}".center(3, " ") if solution_matrix_copy[i][x] > 4 \
                    else f"{solution_matrix_copy[i][x]}".center(3, " ") for x in range(l_map)], sep=" ")

def find_path(the_map):
    best_path = BestPath(math.inf, None)
    # l_map = len(the_map)
    l_map = 16
    solution_matrix = [[0 for _ in range(l_map)] for _ in range(l_map)]
    the_path = []
    if find_path_backtracking(0, 0, l_map, the_map, solution_matrix, the_path, (0,0), 0, True, best_path):
        print(the_path)
        display_steps(l_map, solution_matrix, the_path)
        return True
    else:
        return best_path



if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    the_map = load_map("map.txt")
    # print(the_map[22][22])
    # exit(1)
    # using Dijkstra
    t1 = time()
    the_graph = generate_graph(the_map)
    find_path_v2_heap(the_graph)
    t0 = time()
    print(f"Time needed to find path{t1-t0}")
    print(the_graph.vertex_data[(99, 99)])
    print_graph(the_graph)
    # using backtracking
    # t1 = time()
    # best_path = find_path(the_map)
    # print(f"Best path value {best_path.value}")
    # print(f"Best path {best_path.bestpath}")
    # print(f"Time taken {time()-t1}")

'''
10 - 1.27
11 - 3.226
12 - 7.9 (1.57)
13 - 39.68 (7.28)
14 - 67.41 (11sec; best value 10.53)
15 - 117 (57)
16 - 490 - 8 mins (161)
17 - ???
18 - 632 (222sec; 13.66)
19 - 2340 (583)
20 - 6585
21 - 6404 - 5782
23 - 2757
'''