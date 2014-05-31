from sys import argv

from pydrone.game_engine import Game, DroneKnowledge
from pydrone.utils.matrix_generator import world_generator

from pydrone.contrib.drones import GeometricDrone

# Global parameters


# Algorithm parameters
# ...


def main(size, x, y, drone_x, drone_y, knowledge=False):
    MATRIX_SIZE = int(size)
    END_X = int(x)
    END_Y = int(y)
    START_X = int(drone_x)
    START_Y = int(drone_y)
    KNOWLEDGE = knowledge
    world = world_generator(MATRIX_SIZE, END_X, END_Y, KNOWLEDGE)
    if KNOWLEDGE:
        drones = [DroneKnowledge(world, START_X, START_Y, MATRIX_SIZE)]
    else:
        drones = [GeometricDrone(MATRIX_SIZE, START_X, START_Y)]
    game = Game(world, drones, KNOWLEDGE)
    moves = game.start_game()
    print "Total moves: ", moves

if __name__ == "__main__":
    script, size, x, y, drone_x, drone_y = argv
    main(size, x, y, drone_x, drone_y)
