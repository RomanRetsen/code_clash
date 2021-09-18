import math


class Node:

    def __init__(self, node_name):
        self.name = node_name
        self.distance = math.inf
        self.neighbors = {}

    def add_neighbor(self, neighbor, neighbor_weight):
        if not neighbor in self.neighbors.keys():
            self.neighbors[neighbor] = neighbor_weight

    def __str__(self):
        return f'This is node {self.name}. Current distance {self.distance}. Current neighbors: {self.neighbors}'

class Connection:

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return f'This is connection(edge) between {self.src.name} and {self.dst.name}. Weight is {self.weight}'

class Graph:

    def __init__(self):
        self.all_nodes = {}
        self.all_connections = []

    def add_node(self, node):
        if not node.name in self.all_nodes.keys():
            self.all_nodes[node.name] = node

    def add_nodes_connection(self, src_node, dst_node, weight):
        if src_node.name in self.all_nodes.keys() and dst_node.name in self.all_nodes.keys():
            if not dst_node.name in self.all_nodes[src_node.name].neighbors.keys():
                src_node.add_neighbor(dst_node.name, weight)
                self.all_connections.append(Connection(src_node, dst_node, weight))

    def set_src(self, node_name):
        if node_name in self.all_nodes.keys():
            self.all_nodes[node_name].distance = 0

    def bellman_ford(self, src_name):
        graph.set_src(src_name)
        for _ in range(len(graph.all_nodes) - 1):
            for edge in graph.all_connections:
                print(f"checking {edge}")
                if edge.dst.distance > edge.src.distance + edge.weight:
                    edge.dst.distance = edge.src.distance + edge.weight
                    print(f'Updating {edge.dst}')

        for edge in graph.all_connections:
            if edge.dst.distance > edge.src.distance + edge.weight:
                print("Graph contains negative cycle, meaning result of calculation might be wrong")
                break
        else:
            print("No negative negative cycle were detected. Belman-Ford algorithm succeded")
"""
graph = Graph()
node_a = Node("A")
node_b = Node("B")
node_bb = Node("BB")
node_c = Node("C")
node_cc = Node("CC")
node_d = Node("D")
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_bb)
graph.add_node(node_c)
graph.add_node(node_cc)
graph.add_node(node_d)
graph.add_nodes_connection(node_a, node_b, 2)
graph.add_nodes_connection(node_b, node_bb, 1)
graph.add_nodes_connection(node_a, node_c, 6)
graph.add_nodes_connection(node_c, node_cc, 1)
graph.add_nodes_connection(node_bb, node_d, 3)
graph.add_nodes_connection(node_cc, node_d, -5)
graph.add_nodes_connection(node_d, node_cc, 6)
graph.set_src("A")

for _ in range(len(graph.all_nodes) - 1):
    for edge in graph.all_connections:
        print(f"checking {edge}")
        if edge.dst.distance > edge.src.distance + edge.weight:
            edge.dst.distance = edge.src.distance + edge.weight
            print(f'Updating {edge.dst}')
print(node_d.distance)

for node, node_obj in graph.all_nodes.items():
    print(node_obj)
"""

graph = Graph()
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)
graph.add_node(node_e)

graph.add_nodes_connection(node_a, node_b, -1)
graph.add_nodes_connection(node_b, node_c, 3)
graph.add_nodes_connection(node_a, node_c, 4)
graph.add_nodes_connection(node_b, node_d, 2)
graph.add_nodes_connection(node_d, node_b, 1)
graph.add_nodes_connection(node_d, node_c, 5)
graph.add_nodes_connection(node_e, node_d, -3)
graph.add_nodes_connection(node_b, node_e, 2)
graph.bellman_ford("A")

print(node_e.distance)

for node, node_obj in graph.all_nodes.items():
    print(node_obj)
