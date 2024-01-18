class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = {}

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data):
        new_node = Node(data)
        self.nodes[data] = new_node
        return new_node

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].neighbors[node2] = weight
        self.nodes[node2].neighbors[node1] = weight

    def display(self):
        for node_data, node in self.nodes.items():
            neighbors_data = {neighbor: weight for neighbor, weight in node.neighbors.items()}
            print(f"{node_data} -> {neighbors_data}")

def create_weighted_graph():
    graph = Graph()

    # Menambahkan node
    nodes_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for data in nodes_data:
        graph.add_node(data)

    # Menambahkan edge dengan bobot
    edges = [('a', 'b', 5), ('a', 'e', 2), ('a', 'd', 8),
             ('b', 'c', 10),
             ('c', 'g', 5), ('c', 'e', 3),
             ('d', 'a', 8), ('d', 'h', 3), ('d', 'e', 7),
             ('e', 'h', 1), ('e', 'f', 6)]

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])

    return graph

# Membuat graf dengan bobot
weighted_graph = create_weighted_graph()

# Menampilkan hasil
weighted_graph.display()
