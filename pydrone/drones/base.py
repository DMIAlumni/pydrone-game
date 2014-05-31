class BaseDrone(object):
    """
    Drone interface
    """

    def __init__(self, world_size, x, y):
        self.flipflop = False
        self.last_modifier = 0
        self.actual_position = (x, y)
        self.fuel = 2000
        self.distances = []
        self.last_direction = 0

        # Initialize knoledge base
        self.kb_generator(world_size, x, y)

    def kb_generator(self, world_size, x, y):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def strategy(self):
        raise NotImplementedError()

    def probe(self):
        raise NotImplementedError()

    def print_status(self):
        """
        Not required (ex: optimal algorithm test)
        """
        pass
