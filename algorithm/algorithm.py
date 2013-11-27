from utils.direction_modifier import modifier


def search_far(kb, actual_position, distances, drone):
    X = actual_position[0]
    Y = actual_position[1]
    STEP = len(distances)
    LIMIT = len(kb[0]) - 1

    # Controllo dell'actual_position per sapere se si e' sul bordo
    BORDER_X_R = X == LIMIT
    BORDER_Y_U = Y == LIMIT
    BORDER_X_L = X <= 0
    BORDER_Y_D = Y <= 0

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

    modifier_x = modifier(direction)[0]
    modifier_y = modifier(direction)[1]

    # Cambio del verso del movimento se raggiungo il bordo
    # ad esempio bordo destro, mando x in direzione -1, sinistra
    if BORDER_X_R:
        modifier_x = -1
    if BORDER_X_L:
        modifier_x = 1
    if BORDER_Y_U:
        modifier_y = 1
    if BORDER_Y_D:
        modifier_y = -1

    return X + modifier_x, Y + modifier_y
