from utils.matrix_generator import print_matrix, matrix_generator
from algorithm import search_far


class Drone(object):
    def __init__(self, world_size, x, y):
        self.kb = self.generate_kb(world_size)
        self.graph = matrix_generator(world_size)
        self.graph[x][y] = "S"
        self.actual_position = (x, y)
        self.fuel = 0
        self.distances = []

    def generate_kb(self, world_size):
        return [[0 for i in range(world_size)] for j in range(world_size)]

    def move(self, x, y):
        self.graph[x][y] = "+"
        self.actual_position = (x, y)

    def strategy(self):
        return search_far(self.kb, self.actual_position, self.distances, self)

    def print_world(self):
        print
        print_matrix(self.graph)

    def probe(self, distance):
        self.distances.append(distance)
        self.kb[self.actual_position[0]][self.actual_position[1]] = distance
