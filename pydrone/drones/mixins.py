from pydrone.utils.data_structures import Graph
from pydrone.utils.matrix_generator import matrix_generator


class DroneGraph(object):
    """
    Mixin to use a graph for knowledge base
    """

    def kb_generator(self, world_size, x, y):
        self.graph = matrix_generator(world_size)
        self.graph[x][y] = 1
        self.kb = Graph(x, y)
