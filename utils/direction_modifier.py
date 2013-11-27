def modifier(direction):
#{ 0 : (1,0), 1 : (1,-1), 2 : (0,-1), 3 : (-1,-1), 4 : (-1,0), 5 : (-1,1), 6 : (0,1), 7 : (1,1) }
    if direction == 0:
        return (1, 0)
    elif direction == 1:
        return (1, -1)
    elif direction == 2:
        return (0, -1)
    elif direction == 3:
        return (-1, -1)
    elif direction == 4:
        return (-1, 0)
    elif direction == 5:
        return (-1, 1)
    elif direction == 6:
        return (0, 1)
    elif direction == 7:
        return (1, 1)

def invert_direction(direction):
    return (direction + 4)  % 8
