from game_engine.Game import Game
from game_engine.Drone import Drone
from utils.matrix_generator import world_generator

# Global parameters
MATRIX_SIZE = 20
END_X = 5
END_Y = 10


# Algorithm parameters
# ...

world = world_generator(MATRIX_SIZE, END_X, END_Y)
drones = [Drone(MATRIX_SIZE, 0, 0)]
game = Game(world, drones)
game.start_game()
#print_matrix(game.world)
