import sys


class Graph():

    def __init__(self, vertices):
        self.n_of_vert = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.parent = [None] * vertices

    def print_solution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.n_of_vert):
            print(node, "t", dist[node], "; Parent is: ", self.parent[node])

    def min_distance(self, dist, spt_set):
        min_distance = sys.maxsize
        for v in range(self.n_of_vert):
            if dist[v] < min_distance and spt_set[v] == False:
                min_distance = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.n_of_vert
        dist[src] = 0
        spt_set = [False] * self.n_of_vert

        for cout in range(self.n_of_vert):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.n_of_vert):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    self.parent[v] = u

        self.print_solution(dist)

    def print_path_to(self, dest_vert):
        print(f'Path to final vertix {dest_vert} is:')
        print(f'( {dest_vert} )', end=" ")
        self.recur_search(dest_vert)

    def recur_search(self, dest_vert):
        if self.parent[dest_vert] is None:
            return
        else:
            print("<------", f'( {self.parent[dest_vert]} )', end=" ")
            self.recur_search(self.parent[dest_vert])



g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
g.print_path_to(4)
