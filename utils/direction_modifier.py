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


def modifier(way):
    return directions.get(way)


def fix_direction(x_position, y_position, x_direction, y_direction, world):
    border = len(world[0]) - 1
    new_x = x_position + x_direction
    new_y = y_position + y_direction

    # Cambio direzione

    new_x_direction = x_direction * (-1) if new_x < 0 or new_x > border else x_direction
    new_y_direction = y_direction * (-1) if new_y < 0 or new_y > border else y_direction

    return new_x_direction, new_y_direction
