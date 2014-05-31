from pydrone.utils.matrix_generator import print_matrix
from pydrone.utils.nodes import Graph
from pydrone.algorithm import search_far_calibration, change_strategy
from pydrone.utils.matrix_generator import matrix_generator


class Drone(object):
    def __init__(self, world_size, x, y):
        # self.kb = self.generate_kb(world_size)
        self.flipflop = False
        self.last_modifier = 0
        self.graph = matrix_generator(world_size)
        self.graph[x][y] = 1
        self.actual_position = (x, y)
        self.fuel = 2000
        self.distances = []
        self.last_direction = 0
        # New init, using graph
        self.kb = Graph(x, y)

    def move(self, x, y):
        self.fuel -= 1
        self.actual_position = (x, y)
        self.graph[x][y] += 1
        self.kb.add_node_coord((x, y))

    def strategy(self):
        x, y = search_far_calibration(self)
        # Questo e' uno dei parametri che pesano sull'efficenza
        if self.graph[x][y] <= 1:
            return x, y
        else:
            return change_strategy(self)

    def print_world(self):
        print
        print_matrix(self.graph)

    def probe(self, distance):
        self.distances.append(distance)
        # New probe, with the graph
        self.kb.change_weight(self.actual_position, distance)
