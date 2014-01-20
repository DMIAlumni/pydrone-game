class Game(object):
    def __init__(self, world, drones, knowledge):
        self.k = knowledge
        self.world = world
        self.drones = drones
        self.asset_not_found = True

    def start_game(self):
        i = 0
        while(self.asset_not_found):
            #raw_input()
            drone = self.next_drone()
            # Se il drone chiamato non ha il knowledge, faccio la probe
            if not self.k:
                drone.probe(self.world[drone.actual_position[0]][drone.actual_position[1]])
            #drone.print_world()
            x, y = drone.strategy()
            drone.move(x, y)
            i += 1
            if self.asset_found(x, y) or drone.fuel == 0:
                self.asset_not_found = False
        if drone.fuel == 0:
            return 0
        else:
            return i

    def next_drone(self):
        nextdrone = self.drones.pop()
        self.drones.append(nextdrone)
        return nextdrone

    def asset_found(self, x, y):
        if self.k:
            return self.world[(x, y)][0] == -1
        else:
            return self.world[x][y] == -1
