class Game(object):
    def __init__(self, world, drones):
        self.world = world
        self.drones = drones
        self.asset_not_found = True

    def start_game(self):
        while(self.asset_not_found):
            drone = self.next_drone()
            drone.probe(self.world[drone.actual_position[0]][drone.actual_position[1]])
            x, y = drone.strategy()
            drone.move(x, y)
            drone.print_world()
            if self.asset_found(x, y):
                self.asset_not_found = False
        print "Found!"

    def next_drone(self):
        nextdrone = self.drones.pop()
        self.drones.append(nextdrone)
        return nextdrone

    def asset_found(self, x, y):
        return self.world[x][y] == -1
