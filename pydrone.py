import click

from pydrone.game import SingleAnchorSearchGame
from pydrone.utils.matrix_generator import world_generator

from pydrone.drones.generic import GreedyCompleteDrone
from pydrone.contrib.drones import GeometricDrone


@click.command()
@click.option('--size', default=40, help='Matrix size')
@click.argument('anchor-x', default=5)
@click.argument('anchor-y', default=19)
@click.argument('drone-x', default=30)
@click.argument('drone-y', default=30)
def single_anchor(size, anchor_x, anchor_y, drone_x, drone_y, knowledge=False):
    MATRIX_SIZE = int(size)
    END_X = int(anchor_x)
    END_Y = int(anchor_y)
    START_X = int(drone_x)
    START_Y = int(drone_y)
    KNOWLEDGE = knowledge
    world = world_generator(MATRIX_SIZE, END_X, END_Y, KNOWLEDGE)
    if KNOWLEDGE:
        drones = [GreedyCompleteDrone(world, START_X, START_Y, MATRIX_SIZE)]
    else:
        drones = [GeometricDrone(MATRIX_SIZE, START_X, START_Y)]
    game = SingleAnchorSearchGame(world, drones, KNOWLEDGE)
    moves = game.start_game()
    print "Total moves: ", moves


if __name__ == "__main__":
    single_anchor()
