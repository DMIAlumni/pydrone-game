from utils.direction_modifier import modifier, fix_direction


def search_far_calibration(kb, actual_position, distances, drone):
    x = actual_position[0]
    y = actual_position[1]
    STEP = len(distances)

    if STEP <= 3:

        # Calibrazione non effettuata

        long = 2
        if STEP == 1:
            direction = 0
        elif STEP == 2:
            direction = 2
        elif STEP == 3:
            direction = 5
            long = 1
        print "calibration"
        print distances
        return void_directions(x, y, direction, kb, drone, long)
    else:
        # Calibrazione effettuata, inizio a muovermi
        #
        # Le tre misurazioni della "triangolazione" per capire
        # il quadrante in cui si trova il punto d'arrivo
        first_measure = distances[0]
        second_measure = distances[1]
        third_measure = distances[2]

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

        drone.last_direction = direction
        return go_far(kb, x, y, drone)


def go_far(kb, x, y, drone):
    drone.distances = [] if len(drone.distances) > 4 and drone.distances[-1] > drone.distances[-2] else drone.distances
    return void_directions(x, y, drone.last_direction, kb, drone, 1)


def void_directions(x, y, direction, kb, drone, long):
    # Se non posso andare in una delle direzioni, perche mi trovo al bordo del mondo
    # il fix mi rimanda in quella opposta, e svuoto l'array distances in modo
    # da riniziare da capo la calibrazione in un punto piu conveninete
    try_x_dir, try_y_dir = modifier(direction, long)
    try_x, try_y = x + try_x_dir, y + try_y_dir
    new_x_dir, new_y_dir = fix_direction(x, y, direction, long, kb)
    new_x, new_y = x + new_x_dir, y + new_y_dir
    drone.distances = [] if new_x != try_x or new_y != try_y else drone.distances
    return new_x, new_y


def search_close(kb, actual_position, last_direction, distances):
    X = actual_position[0]
    Y = actual_position[1]
    if len(distances) <= 2:
        direction = (last_direction + 3) % 8
    else:
        direction = last_direction
    mod_x, mod_y = fix_direction(X, Y, direction, 1, kb)
    return X + mod_x, Y + mod_y
