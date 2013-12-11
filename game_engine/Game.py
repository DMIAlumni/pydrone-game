class Game(object):
    def __init__(self, world, drones):
        self.world = world
        self.drones = drones
        self.asset_not_found = True

    def start_game(self):
        i = 0
        while(self.asset_not_found):
            raw_input()
            drone = self.next_drone()
            drone.probe(self.world[drone.actual_position[0]][drone.actual_position[1]])
            drone.print_world()
            x, y = drone.strategy()
            drone.move(x, y)
            i += 1
            if self.asset_found(x, y) or drone.fuel == 0:
                self.asset_not_found = False
        if drone.fuel == 0:
            print 0
        else:
            print i

    def next_drone(self):
        nextdrone = self.drones.pop()
        self.drones.append(nextdrone)
        return nextdrone

    def asset_found(self, x, y):
        return self.world[x][y] == -1
