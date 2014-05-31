from pydrone.utils.direction_modifier import modifier, d


def sum_coord(point, mod):
    mod = modifier(mod, 1)
    return (point[0] + mod[0], point[1] + mod[1])


class Graph(object):
    def __init__(self, x, y):
        self.graph = {}
        self.graph[(x, y)] = (0, 1, 0)
        self.counter = 1
        # Set this to the same amount of Drone.fuel to make
        # the algorithm behave like if there is no optimization
        # If it's less, it will delete nodes when the graph becomes
        # big, saving memory, with a variable increase of the cost
        # of the search algorithm. 20 seemed to be a good choice for
        # this parameter, for matrixes between 5 and 20 of size
        # (obviously not deleting nodes is always better for calculations)
        self.graph_max_length = 2000

    def __getitem__(self, item):
        return self.graph[item]

    def add_node_coord(self, coord):
        self.counter += 1
        if len(self.graph) > self.graph_max_length:
            for node in self.graph:
                if self.graph[node][2] == (self.counter - self.graph_max_length):
                    self.graph.pop(node, None)
                    break
        new_node = Node(coord, 1, self.counter)
        if new_node.k not in self.graph:
            self.graph[new_node.k] = new_node.v
        else:
            old_node = self.graph[coord]
            self.graph[coord] = (old_node[0], old_node[1] + 1, self.counter)
        return new_node.k

    def change_weight(self, coord, w):
        self.graph[coord] = (w, self.graph[coord][1], self.graph[coord][2])

    def print_graph(self):
        for node in self.graph:
            print node, ": ", self.graph[node]

    def goto(self, coord, way):
        new_coord = sum_coord(coord, d[way])
        return self.graph[new_coord] if new_coord in self.graph else -1


class Node(object):
    def __init__(self, k, weight, counter):
        self.k = k
        self.v = (weight, 1, counter)
