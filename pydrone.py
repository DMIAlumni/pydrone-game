import click

from pydrone.game import SingleAnchorSearchGame
from pydrone.utils.matrix_generator import world_generator

from pydrone.drones.generic import GreedyCompleteDrone
from pydrone.contrib.drones import GeometricDrone


@click.command()
@click.option('--size', default=40, help='Matrix size')
@click.option('--knowledge', default=False, help='Use a greedy complete search algorithm')
@click.argument('anchor-x', default=5)
@click.argument('anchor-y', default=19)
@click.argument('drone-x', default=30)
@click.argument('drone-y', default=30)
def single_anchor(size, anchor_x, anchor_y, drone_x, drone_y, knowledge):
    # Generate world
    world = world_generator(size, anchor_x, anchor_y, knowledge)

    # Check if drones should know world values
    if knowledge:
        drones = [GreedyCompleteDrone(size, drone_x, drone_y, world=world)]
    else:
        drones = [GeometricDrone(size, drone_x, drone_y)]

    # Create single anchor search game
    game = SingleAnchorSearchGame(world, drones, knowledge)
    moves = game.start_game()
    print "Total moves: ", moves


if __name__ == "__main__":
    single_anchor()
