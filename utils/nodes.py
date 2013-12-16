from direction_modifier import modifier

def sum_coord(point, mod):
    mod = modifier(mod, 1)
    return (point[0] + mod[0], point[1] + mod[1])

d = {
    "E": 0,
    "NE": 1,
    "N": 2,
    "NO": 3,
    "O": 4,
    "SO": 5,
    "S": 6,
    "SE": 7,
}

class Graph(object):
    def __init__(self):
        self.graph = {}
        self.graph[(0, 0)] = 1

    def __getitem__(self, item):
        return self.graph[item]

    def add_node(self, coord, way):
        way = d[way]
        new_node = Node(sum_coord(coord, way), 1)
        if not self.graph.has_key(new_node.k):
            self.graph[new_node.k] = new_node.v
        else:
            self.graph[new_node.k] = new_node.v + 1
        return new_node.k

    def change_weight(self, coord, w):
        self.graph[coord] = w

    def print_graph(self):
        for node in self.graph:
            print node, ": ", self.graph[node]

    def way(self, coord, way):
        new_coord = sum_coord(coord, d[way])
        return self.graph[new_coord] if self.graph.has_key(new_coord) else -1

class Node(object):
    def __init__(self, k, weight):
        self.k = k
        self.v = weight



graph = Graph()
last_node = (0, 0)
graph.add_node(last_node, "E")
last_node = graph.add_node(last_node, "S")
last_node = graph.add_node(last_node, "SE")
last_node = graph.add_node(last_node, "NO")
last_node = graph.add_node(last_node, "NO")
last_node = graph.add_node(last_node, "N")
last_node = graph.add_node(last_node, "NE")
print last_node
graph.print_graph()
graph.change_weight((1, 0), 12)
print graph.way(last_node, "NE")