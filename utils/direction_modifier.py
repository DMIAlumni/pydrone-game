directions = {
    0: (1, 0),
    1: (1, -1),
    2: (0, -1),
    3: (-1, -1),
    4: (-1, 0),
    5: (-1, 1),
    6: (0, 1),
    7: (1, 1),
}

get_directions = {
    (1, 0): 0,
    (1, -1): 1,
    (0, -1): 2,
    (-1, -1): 3,
    (-1, 0): 4,
    (-1, 1): 5,
    (0, 1): 6,
    (1, 1): 7,
}


d = {
    "E": 0,
    "NE": 1,
    "N": 2,
    "NO": 3,
    "O": 4,
    "SO": 5,
    "S": 6,
    "SE": 7,
}


def get_direction(x_mod, y_mod):
    return get_directions[x_mod, y_mod]


def modifier(way, step):
    return directions.get(way)[0] * step, directions.get(way)[1] * step


def void_directions(x, y, direction, kb, drone, long):
    # Se non posso andare in una delle direzioni, perche mi trovo al bordo del mondo
    # il fix mi rimanda in quella opposta, e svuoto l'array distances in modo
    # da riniziare da capo la calibrazione in un punto piu conveninete
    try_x_dir, try_y_dir = modifier(direction, long)
    new_x_dir, new_y_dir = fix_direction(x, y, direction, long, drone.graph)
    new_x, new_y = x + new_x_dir, y + new_y_dir
    drone.distances = [] if new_x != x + try_x_dir or new_y != y + try_y_dir else drone.distances
    return new_x, new_y


def fix_direction(x_position, y_position, direction, step, world):
    x_direction, y_direction = modifier(direction, step)
    border = len(world[0]) - 1
    new_x = x_position + x_direction
    new_y = y_position + y_direction

    # Cambio direzione

    new_x_direction = x_direction * (-1) if new_x < 0 or new_x > border else x_direction
    new_y_direction = y_direction * (-1) if new_y < 0 or new_y > border else y_direction

    return new_x_direction, new_y_direction

