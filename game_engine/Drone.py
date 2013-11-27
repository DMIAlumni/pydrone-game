from utils.matrix_generator import print_matrix, matrix_generator
from algorithm import search_far, search_close


class Drone(object):
    def __init__(self, world_size, x, y):
        self.kb = self.generate_kb(world_size)
        self.graph = matrix_generator(world_size)
        self.graph[x][y] = 1
        self.actual_position = (x, y)
        self.fuel = 200
        self.distances = []
        self.last_direction = 0

    def generate_kb(self, world_size):
        return [[0 for i in range(world_size)] for j in range(world_size)]

    def move(self, x, y):
        self.fuel -= 1
        self.actual_position = (x, y)
        self.graph[x][y] += 1

    def strategy(self):
        a = float(self.distances[-1])
        if a > 10.000:
            return search_far(self.kb, self.actual_position, self.distances, self)
        else:
            return search_close(self.kb, self.actual_position, self.last_direction, self.distances)

    def print_world(self):
        print
        print_matrix(self.graph)

    def probe(self, distance):
        self.distances.append(distance)
        self.kb[self.actual_position[0]][self.actual_position[1]] = distance
