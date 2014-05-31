import click
import curses


from pydrone.benchmark import Benchmark
from settings import EXECUTION_DRONE, BENCHMARK_DRONE


from pydrone.game import SingleAnchorSearchGame
from pydrone.utils.matrix_generator import world_generator


@click.command()
@click.option('--size', default=40, help='Matrix size')
@click.option('--benchmark', default=False, help='Start benchmark interfaces')
@click.argument('anchor-x', default=5)
@click.argument('anchor-y', default=19)
@click.argument('drone-x', default=30)
@click.argument('drone-y', default=30)
def cli(*args, **kwargs):
    if not kwargs.get('benchmark'):
        game = single_anchor(*args, **kwargs)
        game.start_game()
    else:
        benchmark(*args, **kwargs)


def benchmark(size, anchor_x, anchor_y, drone_x, drone_y, knowledge=False, benchmark=False):
    curses.wrapper(Benchmark(game=single_anchor).start)


def single_anchor(size, anchor_x, anchor_y, drone_x, drone_y, knowledge=False, benchmark=False):
    # Generate world
    world = world_generator(size, anchor_x, anchor_y, knowledge)

    # Check if drones should know world values
    if knowledge:
        drones = [BENCHMARK_DRONE(size, drone_x, drone_y, world=world)]
    else:
        drones = [EXECUTION_DRONE(size, drone_x, drone_y)]

    # Create single anchor search game
    return SingleAnchorSearchGame(world, drones, knowledge, benchmark)


if __name__ == "__main__":
    cli()
