from direction_modifier import modifier, d


def sum_coord(point, mod):
    mod = modifier(mod, 1)
    return (point[0] + mod[0], point[1] + mod[1])


class Graph(object):
    def __init__(self, x, y):
        self.graph = {}
        self.graph[(x, y)] = (0, 1)

    def __getitem__(self, item):
        return self.graph[item]

    def add_node(self, coord, way, probe):
        way = d[way]
        new_node = Node(sum_coord(coord, way), probe)
        if not new_node.k in self.graph:
            self.graph[new_node.k] = new_node.v
        else:
            self.graph[new_node.k] = (new_node.v[0], new_node.v[1] + 1)
        return new_node.k

    def add_node_coord(self, coord):
        new_node = Node(coord, 1)
        if not new_node.k in self.graph:
            self.graph[new_node.k] = new_node.v
        else:
            old_node = self.graph[coord]
            self.graph[coord] = (old_node[0], old_node[1] + 1)
        return new_node.k

    def change_weight(self, coord, w):
        self.graph[coord] = (w, self.graph[coord][1])

    def print_graph(self):
        for node in self.graph:
            print node, ": ", self.graph[node]

    def goto(self, coord, way):
        new_coord = sum_coord(coord, d[way])
        return self.graph[new_coord] if new_coord in self.graph else -1


class Node(object):
    def __init__(self, k, weight):
        self.k = k
        self.v = (weight, 1)



#graph = Graph(12, 32)
#graph.print_graph()
#last_node = (12, 32)
#graph.change_weight((12, 32), 14)
#last_node = graph.add_node(last_node, "E", 13)
#last_node = graph.add_node(last_node, "S", 12)
#last_node = graph.add_node(last_node, "SE", 11)
#last_node = graph.add_node(last_node, "NO", 10)
#last_node = graph.add_node(last_node, "NO", 9)
#last_node = graph.add_node(last_node, "N", 8)
#last_node = graph.add_node(last_node, "NE", 7)
#print graph[(12, 32)][0]
#graph.print_graph()
#print graph.goto(last_node, "NE")
