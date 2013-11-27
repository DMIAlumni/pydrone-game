from utils.direction_modifier import modifier
from utils.direction_modifier import invert_direction


def search_far(kb, actual_position, distances, drone):
    # Controllo dell'actual_position per sapere se si e' sul bordo
    BORDER = False
    GOING_FAR = False
    X = actual_position[0]
    Y = actual_position[1]
    LIMIT = (len(kb[0]) - 1)
    if X == LIMIT or Y == LIMIT or X <= 0 or Y <= 0 :
        BORDER = True
    step = len(distances)
    if step == 1 or step == 2:
        direction = 0
    elif step == 3 or step == 4:
        direction = 2
    elif step == 5:
        direction = 5
    else:
        if distances[-1] > distances[-2]:
            GOING_FAR = True
        dist1 = distances[0]
        dist2 = distances[2]
        dist3 = distances[4]
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
    if GOING_FAR == True:
        drone.distances = []
    if BORDER == True:
        direction = invert_direction(direction)
    return X + modifier(direction)[0], Y + modifier(direction)[1]
