class BaseDrone(object):
    """
    Drone interface
    """

    flipflop = False
    distances = []
    last_direction = 0
    last_modifier = 0
    fuel = 2000

    graph = None
    kb = None
    algorithm = None

    def __init__(self, world_size, x, y):
        # Initialize knowledge base and starting position
        self.actual_position = (x, y)
        self.kb_generator(world_size, x, y)

    def kb_generator(self, world_size, x, y):
        raise NotImplementedError()

    def move(self, x, y):
        raise NotImplementedError()

    def strategy(self):
        raise NotImplementedError()

    def probe(self, distance):
        raise NotImplementedError()

    def print_status(self):
        """
        Not required (ex: optimal algorithm test)
        """
        pass
