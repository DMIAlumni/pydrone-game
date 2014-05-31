from pydrone.drones import BaseDrone
from pydrone.drones.mixins import DroneGraph

from pydrone.algorithms.generic import GreedyCompleteSearch


class GreedyCompleteDrone(DroneGraph, BaseDrone):
    """
    Greedy algorithm with complete information search (used only for benchmark)
    """

    # TODO: create a mixin to choose drone algorithm (better drone interface)
    algorithm = GreedyCompleteSearch()

    def move(self, x, y):
        self.fuel -= 1
        self.actual_position = (x, y)

    def strategy(self):
        x, y = self.algorithm.evaluate(self)
        return x, y
