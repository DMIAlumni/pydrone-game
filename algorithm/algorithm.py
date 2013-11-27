from utils.direction_modifier import modifier


def search_far(kb, actual_position, distances, drone):
    # Variabili

    BORDER_X_R = False
    BORDER_X_L = False
    BORDER_Y_U = False
    BORDER_Y_D = False
    GOING_FAR = False
    LIMIT = (len(kb[0]) - 1)
    X = actual_position[0]
    Y = actual_position[1]
    STEP = len(distances)

    # Controllo dell'actual_position per sapere se si e' sul bordo

    if X == LIMIT:
        BORDER_X_R = True
    if X <= 0:
        BORDER_X_L = True
    if Y == LIMIT:
        BORDER_Y_D = True
    if Y <= 0:
        BORDER_Y_U = True

    # Algoritmo vero e proprio

    if STEP == 1 or STEP == 2:
        direction = 0
    elif STEP == 3 or STEP == 4:
        direction = 2
    elif STEP == 5:
        direction = 5
    else:

        if distances[-1] > distances[-2]:
            GOING_FAR = True

        dist1 = distances[0]
        dist2 = distances[2]
        dist3 = distances[4]
# E se invece di muovermi in una direzione a caso nel quadrante in cui e' supposto essere l'arrivo
# togliessi dal kb tutta quella parte di mondo dove sicuramente non devo andare?
        if dist1 > dist2:
            if dist2 < dist3:
                direction = 7
            elif dist2 > dist3:
                direction = 1
            else:
                direction = 0
        elif dist1 < dist2:
            if dist2 < dist3:
                direction = 5
            elif dist2 > dist3:
                direction = 3
            else:
                direction = 4
        else:
            if dist2 < dist3:
                direction = 6
            elif dist2 > dist3:
                direction = 2
    if GOING_FAR:
        drone.distances = []

    modifier_x = modifier(direction)[0]
    modifier_y = modifier(direction)[1]
    if BORDER_X_R:
        modifier_x = -1
    if BORDER_X_L:
        modifier_x = 1
    if BORDER_Y_U:
        modifier_y = 1
    if BORDER_Y_D:
        modifier_y = -1

    return X + modifier_x, Y + modifier_y
