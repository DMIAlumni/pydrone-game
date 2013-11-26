class Game(object):
    def __init__(self, world, drones):
        self.world = world
        self.drones = drones

    def start_game(self):
        for drone in self.drones:
            drone.probe(self.world[drone.actual_position[0]][drone.actual_position[1]])
            drone.print_world()

        return
