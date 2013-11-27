directions = {
    0 : (1, 0),
    1 : (1, -1),
    2 : (0, -1),
    3 : (-1, -1),
    4 : (-1, 0),
    5 : (-1, 1),
    6 : (0, 1),
    7 : (1, 1),
}


def modifier(way):
    return directions.get(way)


def invert_direction(direction):
    return (direction + 4)  % 8
