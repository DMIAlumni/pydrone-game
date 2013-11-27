from utils.direction_modifier import modifier


def search_far(kb, actual_position, distances):
    step = len(distances)
    if step == 1:
        return (actual_position[0] + modifier(0)[0], actual_position[1] + modifier(0)[1])
    elif step == 2:
        return (actual_position[0] + modifier(0)[0], actual_position[1] + modifier(0)[1])
    elif step == 3:
        return (actual_position[0] + modifier(2)[0], actual_position[1] + modifier(2)[1])
    elif step == 4:
        return (actual_position[0] + modifier(2)[0], actual_position[1] + modifier(2)[1])
    elif step == 5:
        return (actual_position[0] + modifier(5)[0], actual_position[1] + modifier(5)[1])
    else:
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
        return (actual_position[0] + modifier(direction)[0], actual_position[1] + modifier(direction)[1])
