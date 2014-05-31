from pydrone.drones import BaseDrone
from pydrone.drones.mixins import DroneGraph
from pydrone.utils.matrix_generator import print_matrix

from pydrone.contrib.algorithms.geometrical import GeometricAlgorithm


class GeometricDrone(DroneGraph, BaseDrone):
    """
    Federico Dolce GeometricDrone
    """

    # TODO: create a mixin to choose drone algorithm (better drone interface)
    algorithm = GeometricAlgorithm()

    def move(self, x, y):
        self.fuel -= 1
        self.actual_position = (x, y)
        self.graph[x][y] += 1
        self.kb.add_node_coord((x, y))

    def strategy(self):
        x, y = self.algorithm.search_far_calibration(self)

        # This parameter has a great influence on algorithm quality
        if self.graph[x][y] <= 1:
            return x, y
        else:
            return self.algorithm.change_strategy(self)

    def print_world(self):
        # Print current known world and wait for user input before continue
        print_matrix(self.graph)
        raw_input()

    def probe(self, distance):
        self.distances.append(distance)
        self.kb.change_weight(self.actual_position, distance)
