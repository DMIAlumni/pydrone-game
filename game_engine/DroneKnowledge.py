from algorithm import greedy_generic
from utils.matrix_generator import matrix_generator


class DroneKnowledge(object):
    def __init__(self, world, x, y, world_size):
        self.actual_position = (x, y)
        self.graph = matrix_generator(world_size)
        self.fuel = 200
        self.distances = []
        #New init, using graph
        self.kb = world

    def move(self, x, y):
        self.fuel -= 1
        self.actual_position = (x, y)

    def probe(self, distance):
        return 0

    def print_world(self):
        pass

    def strategy(self):
        x, y = greedy_generic(self)
        return x, y