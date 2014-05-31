import math
import fpformat
import os

from pydrone.utils.data_structures import Graph


def world_generator(size, x_end, y_end, knowledge):
    # Controllo se si richiede un mondo con il knowledge degli stati o meno
    if knowledge:
        world = Graph(x_end, y_end)
        for i in range(size):
            for j in range(size):
                world.add_node_coord((i, j))
                world.change_weight((i, j), float(fpformat.fix(math.sqrt(math.fabs(pow((x_end - i), 2) + pow((y_end - j), 2))), 3)))
        world.change_weight((x_end, y_end), -1)
        return world
    else:
        matrix = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                matrix[i][j] = float(fpformat.fix(math.sqrt(math.fabs(pow((x_end - i), 2) + pow((y_end - j), 2))), 3))
        matrix[x_end][y_end] = -1
        return matrix


def world_generator_with_knowledge(size, x_end, y_end):
    world = Graph(x_end, y_end)
    for i in range(size):
        for j in range(size):
            world.add_node_coord((i, j))
            world.change_weight((i, j), float(fpformat.fix(math.sqrt(math.fabs(pow((x_end - i), 2) + pow((y_end - j), 2))), 3)))
    world.change_weight((x_end, y_end), -1)
    return world


def matrix_generator(size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    return matrix


def print_matrix(matrix):
    os.system("clear")
    size = len(matrix[0])
    for j in range(size):
        for i in range(size):
            value = matrix[i][j]
            if value > 0:
                print "", "*",
            else:
                print "", "-",
        print
