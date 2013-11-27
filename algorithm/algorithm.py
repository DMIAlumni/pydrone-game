from utils.direction_modifier import modifier, fix_direction


def search_far(kb, actual_position, distances, drone):
    X = actual_position[0]
    Y = actual_position[1]
    STEP = len(distances)

    if STEP == 1 or STEP == 2:
        direction = 0
    elif STEP == 3 or STEP == 4:
        direction = 2
    elif STEP == 5:
        direction = 5
    else:
        # Le tre misurazioni della "triangolazione" per capire
        # il quadrante in cui si trova il punto d'arrivo
        first_measure = distances[0]
        second_measure = distances[2]
        third_measure = distances[4]

        if first_measure > second_measure:
            if second_measure < third_measure:
                direction = 7
            elif second_measure > third_measure:
                direction = 1
            else:
                direction = 0
        elif first_measure < second_measure:
            if second_measure < third_measure:
                direction = 5
            elif second_measure > third_measure:
                direction = 3
            else:
                direction = 4
        else:
            if second_measure < third_measure:
                direction = 6
            elif second_measure > third_measure:
                direction = 2

        if distances[-1] > distances[-2]:
            drone.distances = []

    modifier_x, modifier_y = modifier(direction)
    drone.last_direction = direction
    modifier_x, modifier_y = fix_direction(X, Y, modifier_x, modifier_y, kb)
    return X + modifier_x, Y + modifier_y


def search_close(kb, actual_position, last_direction, distances):
    X = actual_position[0]
    Y = actual_position[1]
    if len(distances) <= 2:
        direction = (last_direction + 3) % 8
    else:
        direction = last_direction
    mod_x, mod_y = modifier(direction)
    mod_x, mod_y = fix_direction(X, Y, mod_x, mod_y, kb)
    return X + mod_x, Y + mod_y
