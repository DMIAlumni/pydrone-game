from utils.matrix_generator import print_matrix


class Drone(object):
    def __init__(self, world_size, x, y):
        self.kb = self.generate_kb(world_size)
        self.actual_position = (x, y)
        self.fuel = 0

    def generate_kb(self, world_size):
        return [[0 for i in range(world_size)] for j in range(world_size)]

    def move(self, x, y):
        self.actual_position = (x, y)

    def strategy(self):
        pass

    def print_world(self):
        print_matrix(self.kb)

    def probe(self, distance):
        self.kb[self.actual_position[0]][self.actual_position[1]] = distance
