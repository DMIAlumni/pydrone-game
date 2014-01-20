from utils.direction_modifier import void_directions, get_direction, d
import random


def search_far_calibration(kb, actual_position, distances, drone):
    x, y = actual_position
    STEP = len(distances)

    # Calibrazione non effettuata
    if STEP <= 2:
        if STEP == 1:
            direction = d["E"]
        elif STEP == 2:
            direction = d["N"]
        return void_directions(x, y, direction, kb, drone, 1)

    # Calibrazione effettuata, inizio a muovermi
    elif STEP == 3:

        # Le tre misurazioni della "triangolazione" per capire
        # il quadrante in cui si trova il punto d'arrivo

        sud_ovest = distances[0]
        sud_est = distances[1]
        nord_est = distances[2]

        if sud_est < nord_est:
            direction = "S"
        elif sud_est > nord_est:
            direction = "N"
        if sud_ovest > sud_est:
            direction = direction + "E"
        elif sud_ovest < sud_est:
            direction = direction + "O"

        drone.last_direction = d[direction]

    #Questo e' uno dei parametri che pesano sull'efficenza
    # Non toccare ora
    if distances[-1] > 1.0:
        go_x, go_y = go_far(kb, x, y, drone)
    else:
        go_x, go_y = search_close(kb, x, y, drone)

    try:
        if drone.kb[(go_x, go_y)][1] > 2:
            go_x, go_y = change_strategy(drone)
    except:
        pass
    return go_x, go_y



def go_far(kb, x, y, drone):
    dist_param = 1
    if len(drone.distances) > 3 and (drone.distances[-2] - drone.distances[-1]) < dist_param:
        if not (drone.distances[-2] - drone.distances[-1]) == 1:
            if drone.last_modifier == 0:
                rnd = random.random()
                rnd = 1 if rnd < 0.5 else -1
                drone.last_modifier = rnd
            if not drone.flipflop:
                drone.last_direction = (drone.last_direction + drone.last_modifier) % 8
                drone.flipflop = True
            else:
                if drone.distances[-1] > drone.distances[-2]:
                    drone.last_direction = (drone.last_direction + 3) % 8
                else:
                    drone.last_direction = (drone.last_direction + 1) % 8
                drone.flipflop = False
    #drone.distances = [] if len(drone.distances) > 2 and drone.distances[-1] >= drone.distances[-2] else drone.distances
    return void_directions(x, y, drone.last_direction, kb, drone, 1)


def search_close(kb, x, y, drone):
    if drone.last_direction == 1 or drone.last_direction == 7:
        direction = 0
    elif drone.last_direction == 3 or drone.last_direction == 5:
        direction = 4
    else:
        direction = drone.last_direction
    return void_directions(x, y, direction, kb, drone, 1)


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

    go_x, go_y = min(close_distances)[1], min(close_distances)[2]
    return void_directions(x, y, get_direction(go_x - x, go_y - y), drone.kb, drone, 1)
