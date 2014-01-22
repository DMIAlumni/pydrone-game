from sys import argv

from game_engine import Game, Drone, DroneKnowledge
from utils.matrix_generator import world_generator

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
        drones = [Drone(MATRIX_SIZE, START_X, START_Y)]
    game = Game(world, drones, KNOWLEDGE)
    return game.start_game()

#if __name__ == "__main__":
#    script, size, x, y, drone_x, drone_y = argv
#    main(size, x, y, drone_x, drone_y)