import pygame
import cv2
import math
import heapq
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np


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
    the_path = r"/home/romio/Downloads/images"
    def __init__(self):
        self.all_edges = {}
        self.all_vertex = {}
        self.starting_vertex_coord = None

    @staticmethod
    def load_map_from_picture(file):

        img = cv2.imread(f"{Graph.the_path}/{file}", 0)
        target_0 = cv2.imread(f"{Graph.the_path}/goal00.png", 0)
        target_1 = cv2.imread(f"{Graph.the_path}/goal01.png", 0)
        target_2 = cv2.imread(f"{Graph.the_path}/goal02.png", 0)
        target_3 = cv2.imread(f"{Graph.the_path}/goal03.png", 0)
        wall_0 = cv2.imread(f"{Graph.the_path}/wall00.png", 0)
        wall_1 = cv2.imread(f"{Graph.the_path}/wall01.png", 0)
        wall_2 = cv2.imread(f"{Graph.the_path}/wall02.png", 0)
        wall_3 = cv2.imread(f"{Graph.the_path}/wall03.png", 0)
        start_0 = cv2.imread(f"{Graph.the_path}/start00.png", 0)
        start_1 = cv2.imread(f"{Graph.the_path}/start01.png", 0)
        start_2 = cv2.imread(f"{Graph.the_path}/start02.png", 0)
        start_3 = cv2.imread(f"{Graph.the_path}/start03.png", 0)
        target_0_res = [x[::8] for x in cv2.matchTemplate(img, target_0, cv2.TM_CCOEFF_NORMED)[::8]]
        target_1_res = [x[::8] for x in cv2.matchTemplate(img, target_1, cv2.TM_CCOEFF_NORMED)[::8]]
        target_2_res = [x[::8] for x in cv2.matchTemplate(img, target_2, cv2.TM_CCOEFF_NORMED)[::8]]
        target_3_res = [x[::8] for x in cv2.matchTemplate(img, target_3, cv2.TM_CCOEFF_NORMED)[::8]]
        wall_0_res = [x[::8] for x in cv2.matchTemplate(img, wall_0, cv2.TM_CCOEFF_NORMED)[::8]]
        wall_1_res = [x[::8] for x in cv2.matchTemplate(img, wall_1, cv2.TM_CCOEFF_NORMED)[::8]]
        wall_2_res = [x[::8] for x in cv2.matchTemplate(img, wall_2, cv2.TM_CCOEFF_NORMED)[::8]]
        wall_3_res = [x[::8] for x in cv2.matchTemplate(img, wall_3, cv2.TM_CCOEFF_NORMED)[::8]]
        start_0_res = [x[::8] for x in cv2.matchTemplate(img, start_0, cv2.TM_CCOEFF_NORMED)[::8]]
        start_1_res = [x[::8] for x in cv2.matchTemplate(img, start_1, cv2.TM_CCOEFF_NORMED)[::8]]
        start_2_res = [x[::8] for x in cv2.matchTemplate(img, start_2, cv2.TM_CCOEFF_NORMED)[::8]]
        start_3_res = [x[::8] for x in cv2.matchTemplate(img, start_3, cv2.TM_CCOEFF_NORMED)[::8]]
        the_dict = {}
        the_dict[0] = target_0_res
        the_dict[1] = target_1_res
        the_dict[2] = target_2_res
        the_dict[3] = target_3_res
        the_dict[4] = wall_0_res
        the_dict[5] = wall_1_res
        the_dict[6] = wall_2_res
        the_dict[7] = wall_3_res
        the_dict[8] = start_0_res
        the_dict[9] = start_1_res
        the_dict[10] = start_2_res
        the_dict[11] = start_3_res
        map_h, map_w = img.shape[:]
        h, w = target_0.shape[:]
        data_map_w = (map_w - w + 1) // w
        data_map_h = (map_h - h + 1) // h

        the_map = [[None for _ in range(data_map_w + 1)] for _ in range(data_map_h + 1)]

        detected_start_coord = None
        detected_end_coord = None
        for i in range(data_map_h + 1):
            for y in range(data_map_w + 1):
                most_probable_value = max(((index, the_dict[index][i][y]) for index in the_dict), key=lambda x: x[1])
                if most_probable_value[0] in (0,1,2,3):
                    print(f"Target found at {i}:{y}")
                    detected_end_coord = (i,y)
                if most_probable_value[0] in (8,9,10,10):
                    print(f"Start found at {i}:{y}")
                    detected_start_coord = (i,y)
                the_map[i][y] = Tile(most_probable_value[0], None)

        if detected_start_coord is None or detected_end_coord is None:
            print(f"Failed to find starting or ending points")
            exit(1)
        return (detected_start_coord, detected_end_coord, the_map)

    def load_vertices(self, the_map):
        the_l_i = len(the_map)
        the_l_y = len(the_map[0])

        for i in range(the_l_i):
            for y in range(the_l_y):
                new_vertex = Vertex(i, y)
                self.add_vertex(new_vertex)

        for vertex in self.all_vertex.values():
            vertex_coord = vertex.get_vertex_coord()
            neighbour_to_south_coord = (vertex_coord[0] + 1, vertex_coord[1])
            neighbour_to_north_coord = (vertex_coord[0] - 1, vertex_coord[1])
            neighbour_to_west_coord = (vertex_coord[0], vertex_coord[1] - 1)
            neighbour_to_east_coord = (vertex_coord[0], vertex_coord[1] + 1)
            if neighbour_to_south_coord in self.all_vertex \
                    and not (the_map[neighbour_to_south_coord[0]][neighbour_to_south_coord[1]].type in (0,2,4,6,8,10)):
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_south_coord],1))
                vertex.add_neighbour(self.all_vertex[neighbour_to_south_coord])
            if neighbour_to_north_coord in self.all_vertex \
                    and not (the_map[vertex_coord[0]][vertex_coord[1]].type in (0,2,4,6,8,10)):
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_north_coord], 1))
                vertex.add_neighbour(self.all_vertex[neighbour_to_north_coord])
            if neighbour_to_east_coord in self.all_vertex \
                    and not (the_map[neighbour_to_east_coord[0]][neighbour_to_east_coord[1]].type in (0,1,4,5,8,9)):
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_east_coord], 1))
                vertex.add_neighbour(self.all_vertex[neighbour_to_east_coord])
            if neighbour_to_west_coord in self.all_vertex \
                    and not (the_map[vertex_coord[0]][vertex_coord[1]].type in (0,1,4,5,8,9)):
                self.add_edge(Edge(vertex, self.all_vertex[neighbour_to_west_coord], 1))
                vertex.add_neighbour(self.all_vertex[neighbour_to_west_coord])
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
            unresolved_verteces = [(vrtx.cost, index, vrtx) for _,index,vrtx in unresolved_verteces]
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
        the_map = [[1 if not x == -1 else -1 for x in y] for y in the_map]
        print(*the_map, end="\n")
        H = np.array(the_map)
        plt.imshow(H, interpolation='none')
        plt.show()

    def display_path_to_destination_pygame(self, x, y, the_map, maze_file):
        end_coord = (x,y)
        the_path = []
        while not (path_element_coord := self.all_vertex[end_coord].parent.get_vertex_coord()) == \
                  self.starting_vertex_coord:
            the_path.append(path_element_coord)
            end_coord = path_element_coord
        else:
            the_path.append(path_element_coord)
        the_l_i = len(the_map)
        the_l_y = len(the_map[0])

        pygame.init()
        clock = pygame.time.Clock()
        game_h = the_l_i * 8 * 2
        game_w = the_l_y * 8 * 2
        scrn = pygame.display.set_mode((game_w, game_h))
        pygame.display.set_caption('Finding path')
        imp = pygame.transform.scale(pygame.image.load(f"{Graph.the_path}/{maze_file}"), (game_w, game_h))
        scrn.blit(imp, (0, 0))
        pygame.display.flip()
        status = True
        while (status):
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False
            for step in the_path[::-1][1:]:
                pygame.draw.circle(scrn, 'red', (step[1] * 8 * 2 + 8, step[0] * 8 * 2 + 8), 5, 4)
                pygame.display.flip()
                clock.tick(25)
        pygame.quit()


class Tile:
    def __init__(self, type, mask):
        '''tile mask is used in bit-wise AND operation'''
        self.type = type
        self.tile_mask = mask

    def __repr__(self):
        description = ""
        if self.type == 0:
            description = f"Target with wall on top and left"
        elif self.type == 1:
            description = f"Target with on left"
        elif self.type == 2:
            description = f"Target with wall on top"
        elif self.type == 3:
            description = f"Target with no walls"
        elif self.type == 4:
            description = f"Wall on top and left"
        elif self.type == 5:
            description = f"Wall on the lelf"
        elif self.type == 6:
            description = f"Wall on the top"
        elif self.type == 7:
            description = f"No wall"
        elif self.type == 8:
            description = f"Start with wall on top and left"
        elif self.type == 9:
            description = f"Start with wall on the left"
        elif self.type == 10:
            description = f"Start with wall on the top"
        elif self.type == 11:
            description = f"Start with no wall"
        return description


def main():
    maze_file = "snailmaze00.png"
    new_graph = Graph()
    starting_point, target_point, the_map = Graph.load_map_from_picture(maze_file)
    new_graph.load_vertices(the_map)
    new_graph.assign_starting_vertex(starting_point[0], starting_point[1])
    new_graph.build_network()
    new_graph.display_path_to_destination_pygame(target_point[0], target_point[1], the_map[:], maze_file)



if __name__ == "__main__":
    main()