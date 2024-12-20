import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        # print(f'all neighbor  {(self.adjacent)}')
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        # print(type(neighbor))
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + " adjacent: " + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous

import heapq

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start, target):
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(), index, v) for index,v in enumerate(aGraph)]
    heapq.heapify(unvisited_queue)
    while len(unvisited_queue):
        print(unvisited_queue)
        uv = heapq.heappop(unvisited_queue)
        current = uv[2]
        current.set_visited()
        print(f"current node {current}")
        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print("updated: current = %s next = %s new_dist = %s" \
                      %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print("not updated: current = %s next = %s new_dist = %s" \
                      %(current.get_id(), next.get_id(), next.get_distance()))

        # while len(unvisited_queue):
        #     heapq.heappop(unvisited_queue)
        unvisited_queue.clear()
        unvisited_queue = [(v.get_distance(), index, v) for index, v in enumerate(aGraph) if not v.visited]
        heapq.heapify(unvisited_queue)

if __name__ == "__main__":
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")

    g.add_edge("a", "b", 2)
    g.add_edge("a", "c", 6)
    g.add_edge("b", "d", 3)
    g.add_edge("c", "d", -5)


    print("Graph Data: ")
    for node in g:
        for neighbor in node.get_connections():
            node_id = node.get_id()
            # neighbor_id = neighbor.get_id()
            print("(%s, %s, %3d)" %(node_id, neighbor, node.get_weight(neighbor)))

    dijkstra(g, g.get_vertex("a"), g.get_vertex("e"))
    target = g.get_vertex("d")
    path = [target.get_id()]
    shortest(target, path)
    print("Shortest path: %s" %(path[::-1]))
"""
if __name__ == "__main__":
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_vertex("f")
    g.add_edge("a", "b", 7)
    g.add_edge("a", "c", 9)
    g.add_edge("a", "f", 14)
    g.add_edge("b", "c", 10)
    g.add_edge("b", "d", 15)
    g.add_edge("c", "d", 11)
    g.add_edge("c", "f", 2)
    g.add_edge("d", "e", 6)
    g.add_edge("e", "f", 9)
    print("Graph Data: ")
    for node in g:
        for neighbor in node.get_connections():
            node_id = node.get_id()
            # neighbor_id = neighbor.get_id()
            print("(%s, %s, %3d)" %(node_id, neighbor, node.get_weight(neighbor)))
    dijkstra(g, g.get_vertex("a"), g.get_vertex("e"))
    target = g.get_vertex("e")
    path = [target.get_id()]
    shortest(target, path)
    print("Shortest path: %s" %(path[::-1]))
"""