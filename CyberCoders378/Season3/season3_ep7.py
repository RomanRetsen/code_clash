import heapq
import math
import os
import cv2
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from Tile import Tile


# Function visualize_map
# Use matplot lib module to create plot that indicate all walls using rectangles; connections between tiles (with
#   arrow); and the path using a blue highlight
# Input : map_tiles : the list of list of Tile object, properly graphed
#         width_tiles : the size in width of the map_tiles 2D array
#         height_tiles : the size in height of the map_tiles 2D array
#         path to visualize : when input, it will display the path in blue
def visualize_map(map_tiles, width_tiles, height_tiles, path=None):
    # Some initialisations

    # Loop through all tiles to draw it

            # Draw a rectangle for the each tile

            # Draw a "S" for start and a "G" for goal
            # Draw The arrows depending if there are not any wall (opening) on the north, east, south and west side

    # Draw the path if provided
    # Prepare the plot to be display in a new window
    ...


# Function build_graph
# Using the images of walls (wall##.png), it performs cv2.matchTemplate on each tiles of the maze to detect what type of
# wall it is at each block
# Input : img_gray : Image of the maze loaded and converted to grayscale
#         width : Width of the whole maze
#         height : Height of the whole maze
# Output : 2D array of Tile objects
# def build_graph(img_gray, width, height) -> list[list[Tile]]:
    # load all 4 wall##.png as grayscaled images using cv2

    # Initialize a list of list tilemap with value -1.
    # Loop though the maze image, 8x8 pixel bloc at a time, cutting it from the image to they compare it with each of
    # the walls. For each wal tested, take the one that has the highest result, and that is that idx (00 - 03) that will
    # be place in that tilemap position.

    # Once we have an 2D array of idx (00-03) we can use that to create another 2D array of Tile objects this time.

    # And return that 2D array of Tile Obj
    ...


# Function find_goal
# Using the images of walls (goal##.png), it performs cv2.matchTemplate on the whole maze image to find at which
# location the goal might be located
# Input : img_maze : Image of the maze loaded in color
# Output : (int, int) : the location in tile x and y of the goal
def find_goal(img_maze) -> (int, int):
    ...


# Function find_start
# Using the images of walls (start##.png), it performs cv2.matchTemplate on the whole maze image to find at which
# location the start might be located
# Input : img_maze : Image of the maze loaded in color
# Output : (int, int) : the location in tile x and y of the start
def find_start(img_maze) -> (int, int):
    ...


# Function pathfinding
# The heart of the Dijkstra's algorithm.
# Input : map_tiles : the 2D Array of Tile objects
#         pos_start : (int, int) start position of the maze
#         pos_goal : (int, int) goal position of the maze
# Output : list : the path found
def pathfinding(map_tiles, pos_start, pos_goal) -> list:
    # get start and goal tile objects

    # Priority queue to store the tiles to be processed

    # Dictionary to store the previous tile for each tile

    # Loop while the queue is not empty
        # Pop from the priority queue

        # If we are at destination, break

        # Loop Through all the current tile neighbours
                # Assuming each move has a cost of 1

                # If the neighboor greater distance than current distance, set it and push it to the queue,
                # update previous tiles

    # Reconstruct the path, from previous_tiles array

    # return the path
    ...

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_resolved = False
        self.parent = None
        self.cost = math.inf
        self.neighbours = {}
        
    def add_neighbour(self, neighbour):
        if not (neighbour.x, neighbour.y) in self.neighbours:
            self.neighbours[(neighbour.x, neighbour.y)] = neighbour

    def assign_parent_and_cost(self, parent, cost):
        self.parent = parent
        self.cost = cost

    def mark_resolved(self):
        self.is_resolved = True

    def get_vertex_coord(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"The Vertex. Coord: {self.x}:{self.y}. Current cost: {self.cost}"

class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

    def get_edge_coord(self):
        return self.start_vertex.get_vertex_coord() + self.end_vertex.get_vertex_coord()

    def __repr__(self):
        return f"The Edge. From vertex: {self.start_vertex.x}:{self.start_vertex.y}. \
                To Vertex: {self.end_vertex.x}:{self.end_vertex.y}"

class Graph:
    def __init__(self):
        self.all_edges = {}
        self.all_vertex = {}
        self.starting_vertex_coord = None

    @staticmethod
    def load_map_from_file(file):
        the_map = []
        with open(file) as file:
            for line in file:
                the_map.append([float(x) for x in line.strip().split()])
        return the_map

    def load_vertices(self, the_map):
        the_l_i = len(the_map)
        the_l_y = len(the_map[0])

        for i in range(the_l_i):
            for y in range(the_l_y):
                if the_map[i][y] < 1:
                    new_vertex = Vertex(i, y)
                    self.add_vertex(new_vertex)

        for vertex in self.all_vertex.values():
            vertex_coord = vertex.get_vertex_coord()
            neighbour_to_south_coord = (vertex_coord[0]-1, vertex_coord[1])
            neighbour_to_north_coord = (vertex_coord[0]+1, vertex_coord[1])
            neighbour_to_west_coord = (vertex_coord[0], vertex_coord[1]+1)
            neighbour_to_east_coord = (vertex_coord[0], vertex_coord[1]-1)
            if neighbour_to_south_coord  in  self.all_vertex:
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_south_coord], \
                                   the_map[neighbour_to_south_coord[0]][neighbour_to_south_coord[1]]))
                vertex.add_neighbour(self.all_vertex[neighbour_to_south_coord])
            if neighbour_to_north_coord  in  self.all_vertex:
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_north_coord], \
                                   the_map[neighbour_to_north_coord[0]][neighbour_to_north_coord[1]]))
                vertex.add_neighbour(self.all_vertex[neighbour_to_north_coord])
            if neighbour_to_east_coord  in  self.all_vertex:
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_east_coord], \
                                   the_map[neighbour_to_east_coord[0]][neighbour_to_east_coord[1]]))
                vertex.add_neighbour(self.all_vertex[neighbour_to_east_coord])
            if neighbour_to_west_coord  in  self.all_vertex:
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_west_coord], \
                                   the_map[neighbour_to_west_coord[0]][neighbour_to_west_coord[1]]))
                vertex.add_neighbour(self.all_vertex[neighbour_to_west_coord])

    def build_network(self):
        unresolved_verteces = [(vrtx.cost, index, vrtx) for index, vrtx in enumerate(self.all_vertex.values())]
        heapq.heapify(unresolved_verteces)
        while len(unresolved_verteces):
            current = heapq.heappop(unresolved_verteces)[2]
            current.mark_resolved()
            for neighbour in current.neighbours.values():
                if neighbour.is_resolved:
                    continue
                new_distance = current.cost + self.get_edge_weight(current, neighbour)
                if new_distance < neighbour.cost:
                    neighbour.assign_parent_and_cost(current, new_distance)
                    # neighbour.cost = new_distance
                    # neighbour.parent = current
            heapq.heapify(unresolved_verteces)

    def display_path_to_destination(self, x, y, the_map):
        end_coord = (x,y)
        the_map[x][y] = -1
        while not (path_element_coord := self.all_vertex[end_coord].parent.get_vertex_coord()) == \
                  self.starting_vertex_coord:
            the_map[path_element_coord[0]][path_element_coord[1]] = -1
            end_coord = path_element_coord
        else:
            the_map[self.starting_vertex_coord[0]][self.starting_vertex_coord[1]] = -1
        H = np.array(the_map)
        plt.imshow(H, interpolation='none')
        plt.show()


    def assign_starting_vertex(self, x, y):
        if (x,y) in self.all_vertex:
            self.get_vertex_by_coord(x,y).cost = 0
            self.starting_vertex_coord = (x, y)
        else:
            print(f"Error assigning starting vertex. Check if such vertex exist")
            exit(1)

    def get_vertex_by_coord(self, x, y):
        return self.all_vertex[(x,y)]

    def add_edge(self, edge):
        if not edge.get_edge_coord() in self.all_edges:
            self.all_edges[edge.start_vertex.get_vertex_coord() + edge.end_vertex.get_vertex_coord()] = edge
        else:
            print(f"Attempt to add existent edge.  start:{edge.start_vertex.x}:{edge.start_vertex.y};\
                    end:{edge.end_vertex.x}:{edge.end_vertex.y}.")

    def add_vertex(self, vertex):
        if not vertex.get_vertex_coord() in self.all_vertex:
            self.all_vertex[vertex.get_vertex_coord()] = vertex
        else:
            print(f"existent vertexted attempt to add {vertex.x}{vertex.y}")
            exit(1)

    def get_edge_weight(self, start_vertex, end_vertex):
        return self.all_edges[start_vertex.get_vertex_coord() +  end_vertex.get_vertex_coord()].weight



def main2():
    new_graph = Graph()
    the_map = Graph.load_map_from_file("../Season2/map.txt")
    new_graph.load_vertices(the_map)
    new_graph.assign_starting_vertex(0,0)
    new_graph.build_network()
    new_graph.display_path_to_destination(99,99, the_map[:])


def main():
    sum_paths = 0
    for i in range(12):

        # Read snailmaze## in subdirectory 'image'
        filename = os.path.join(".", "images", "snailmaze{:02d}.png".format(i))
        img = cv2.imread(filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # call function to find the location of the start of the maze
        pos_start = find_start(img)
        print(pos_start)

        # call function to find the location of the goal of the maze
        pos_goal = find_goal(img)
        print(pos_goal)

        # call the function to build the Tiles array, and set the start and goal attribute accordingly
        map_tiles: [[Tile]] = build_graph(img_gray, 241, 129)
        map_tiles[pos_goal[1]][pos_goal[0]].is_goal = True
        map_tiles[pos_start[1]][pos_start[0]].is_start = True

        # call the pathfinding function to find the path in the maze. As a verification, let's get the total number
        # of step to each map to check that we properly accomplish the pathfinding algorithm
        path = pathfinding(map_tiles, pos_start, pos_goal)
        sum_paths += len(path)
        print(f"len(path) = {len(path)}")

        #As a bonus we want to display the path with matplotlib
        visualize_map(map_tiles, 30, 16, path)

    # return the sum of all the path lenghts
    print(sum_paths)

if __name__ == '__main__':
    # main()
    main2()
