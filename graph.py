class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node2][node1] = weight

    def get_neighbors(self, node):
        return self.graph.get(node, {})
