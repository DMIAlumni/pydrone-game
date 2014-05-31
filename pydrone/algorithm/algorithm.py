import random

from pydrone.utils.direction_modifier import void_directions, get_direction, d


def search_far_calibration(drone):

    distances = drone.distances
    STEP = len(distances)

    # Calibrazione non effettuata

    if STEP <= 2:

        direction = d["E"] if STEP == 1 else d["N"] if STEP == 2 else drone.last_direction
        return void_directions(direction, drone)

    # Calibrazione effettuata, inizio a muovermi

    elif STEP == 3:

        # Le tre misurazioni della "triangolazione" per capire
        # il quadrante in cui si trova il punto d'arrivo

        sud_ovest, sud_est, nord_est = distances[:3]
        direction = "S" if sud_est < nord_est else "N" if sud_est > nord_est else ""
        direction += "E" if sud_ovest > sud_est else "O" if sud_ovest < sud_est else ""
        drone.last_direction = d[direction]

    return go_far(drone) if distances[-1] > 1.0 else search_close(drone)


def go_far(drone):

    if len(drone.distances) > 3 and (drone.distances[-2] - drone.distances[-1]) < 1:

        if drone.last_modifier == 0:

            drone.last_modifier = 1 if random.random() < 0.5 else -1

        if not drone.flipflop:

            drone.flipflop, drone.last_direction = (True, (drone.last_direction + drone.last_modifier) % 8)

        else:

            mod = 3 if drone.distances[-1] > drone.distances[-2] else 1
            drone.flipflop, drone.last_direction = (False, (drone.last_direction + mod) % 8)

    if len(drone.distances) > 3 and (drone.distances[-2] - drone.distances[-1]) > 1 and drone.flipflop:

        drone.flipflop, drone.last_direction = (True, (drone.last_direction - drone.last_modifier) % 8)

    else:

        drone.flipflop = True

    return void_directions(drone.last_direction, drone)


def search_close(drone):

    direction = (0 if drone.last_direction == 1 or drone.last_direction == 7 else
                 4 if drone.last_direction == 3 or drone.last_direction == 5 else drone.last_direction)

    return void_directions(direction, drone)


def change_strategy(drone):

    drone.distances = []
    x, y = drone.actual_position
    close_distances = []

    # Controllo in quale dei punti adiacenti sono passato meno volte

    for x_index in (x - 1, x, x + 1):
        for y_index in (y - 1, y, y + 1):

            # Se il punto e' accessibile, e non e' il punto stesso in cui sono partito
            # viene aggiunto all'array

            if x_index >= 0 and x_index < len(drone.graph[0]) and y_index >= 0 and y_index < len(drone.graph[0]):
                if x_index != x or y_index != y:

                    # Questo array conterra' tutti i punti adiacenti ed accessibili

                    try:
                        close_distances.append([drone.kb[(x_index, y_index)][1], x_index, y_index])
                    except:
                        close_distances.append([0, x_index, y_index])

    # Vado verso il primo dei punti in cui sono passato meno volte

    return void_directions(get_direction(min(close_distances)[1] - x, min(close_distances)[2] - y), drone)
