import sys
from common.intcode import Intcode
import numpy as np


def turn_left(x, y, facing):
    if facing == 'U':
        return x - 1, y, 'L'
    elif facing == 'L':
        return x, y - 1, 'D'
    elif facing == 'D':
        return x + 1, y, 'R'
    elif facing == 'R':
        return x, y + 1, 'U'
    else:
        raise RuntimeError('Unknown facing arg: {}'.format(facing))


def turn_right(x, y, facing):
    if facing == 'U':
        return x + 1, y, 'R'
    elif facing == 'L':
        return x, y + 1, 'U'
    elif facing == 'D':
        return x - 1, y, 'L'
    elif facing == 'R':
        return x, y - 1, 'D'
    else:
        raise RuntimeError('Unknown facing arg: {}'.format(facing))


def paint_panels(robot_program, start_color=0):
    x, y = 0, 0
    panels = {}
    facing = 'U'

    panels[(x, y)] = start_color

    while not robot_program.is_halted():
        if (x, y) in panels:
            color = panels[(x, y)]
        else:
            color = panels[(x, y)] = 0

        color, direction = robot_program.execute(color)

        panels[(x, y)] = color

        if direction == 0:
            x, y, facing = turn_left(x, y, facing)
        else:
            x, y, facing = turn_right(x, y, facing)

    return panels


def build_image(panels):
    max_x, max_y = -sys.maxsize, -sys.maxsize
    min_x, min_y = sys.maxsize, sys.maxsize

    for panel in panels:
        max_x, max_y = max(max_x, panel[0]), max(max_y, panel[1])
        min_x, min_y = min(min_x, panel[0]), min(min_y, panel[1])

    width = abs(max_x - min_x) + 1
    height = abs(max_y - min_y) + 1

    image = np.zeros((height, width))

    for coord, color in panels.items():
        x, y = coord

        x = abs(x)
        y = abs(y)

        image[y][x] = color

    return image


def print_image(image):
    for row in image:
        print('{}'.format(''.join(map(str, row)).replace('0', ' ')))


def main():
    program = Intcode('input')
    print('Answer for Day11 - Part 1: {}'.format(len(paint_panels(program))))

    print('Answer for Day11 - Part 2:')
    program.reset()
    panels = paint_panels(program, 1)
    image = build_image(panels)
    print_image(image)


if __name__ == "__main__":
    main()
