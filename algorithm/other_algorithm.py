from utils.direction_modifier import void_directions, get_direction


def greedy_generic(drone):
    x, y = drone.actual_position
    available = []
    for x_index in (x - 1, x, x + 1):
        for y_index in (y - 1, y, y + 1):
            if x_index >= 0 and x_index < len(drone.graph[0]) and y_index >= 0 and y_index < len(drone.graph[0]):
                if x_index != x or y_index != y:
                        available.append([drone.kb[(x_index, y_index)][0], x_index, y_index])

    go_x, go_y = min(available)[1], min(available)[2]
    return void_directions(get_direction(go_x - x, go_y - y), drone)
