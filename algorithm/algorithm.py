from utils.direction_modifier import void_directions


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
        return void_directions(x, y, direction, kb, drone, long)
    elif STEP == 4:
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
    if distances[-1] > 2.0:
        return go_far(kb, x, y, drone)
    else:
        return search_close(kb, x, y, drone)


def go_far(kb, x, y, drone):
    drone.distances = [] if len(drone.distances) > 4 and drone.distances[-1] > drone.distances[-2] else drone.distances
    return void_directions(x, y, drone.last_direction, kb, drone, 1)


def search_close(kb, x, y, drone):
    if drone.last_direction == 1 or drone.last_direction == 7:
        direction = 0
    elif drone.last_direction == 3 or drone.last_direction == 5:
        direction = 4
    else:
        direction = drone.last_direction
    return void_directions(x, y, direction, kb, drone, 1)
