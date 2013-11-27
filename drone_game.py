from sys import argv

from game_engine import Game, Drone
from utils.matrix_generator import world_generator

# Global parameters
script, size, x, y, drone_x, drone_y = argv

MATRIX_SIZE = int(size)
END_X = int(x)
END_Y = int(y)
START_X = int(drone_x)
START_Y = int(drone_y)


# Algorithm parameters
# ...

world = world_generator(MATRIX_SIZE, END_X, END_Y)
drones = [Drone(MATRIX_SIZE, START_X, START_Y)]
game = Game(world, drones)
game.start_game()
