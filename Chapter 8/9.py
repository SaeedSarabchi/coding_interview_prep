def paint_fill(screen, point, new_color):
    rec_paint_fill(screen, point, screen[point[0]][point[1]], new_color)


def rec_paint_fill(screen, point, orig_color, new_color):
    if (not is_valid_point(point, (len(screen), len(screen[0])))) or screen[point[0]][point[1]] != orig_color:
        return
    #set color
    screen[point[0]][point[1]] = new_color
    #go up
    new_point = (point[0], point[1]-1)
    rec_paint_fill(screen, new_point, orig_color, new_color)
    # go down
    new_point = (point[0], point[1] + 1)
    rec_paint_fill(screen, new_point, orig_color, new_color)
    # go left
    new_point = (point[0]-1, point[1])
    rec_paint_fill(screen, new_point, orig_color, new_color)
    # go right
    new_point = (point[0]+1, point[1])
    rec_paint_fill(screen, new_point, orig_color, new_color)


def is_valid_point(input_point, size_tuple):
    #first arg out of bounds
    if input_point[0]<0 or input_point[0]>=size_tuple[0]:
        return False
    #second arg out of bounds
    if input_point[1]<0 or input_point[1]>=size_tuple[1]:
        return False
    return True


screen = [[2,2,1,1],[2,0,0,2],[2,0,0,1],[2,0,0,0]]
paint_fill(screen, (2,2), 4)
print(screen)

