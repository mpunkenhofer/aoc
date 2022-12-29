from typing import Tuple
from src.common.util import read_input
import sys

ScanDataType = list[list[Tuple[int, int]]]
MapType = list[list[str]]
PointType = Tuple[int, int]

def parse_scan(data: list[str]) -> ScanDataType:
    result = []

    for line in data:
        coords = line.split(' -> ')
        path = []

        for c in coords:
            x, y = c.split(',')
            path.append((int(x), int(y)))

        result.append(path)

    return result

def get_dimensions(scan: ScanDataType) -> Tuple[PointType]:
    max_x = max_y = 0
    min_x = min_y = sys.maxsize

    for path in scan:
        for x,y in path:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
    
    return ((min_x, min_y), (max_x, max_y))

def draw_wall(m: MapType, start: PointType, end: PointType):
    sx, sy = start
    ex, ey = end

    if sy - ey == 0:
        for x in range(min(sx, ex), max(sx, ex) + 1):
            m[ey][x] = '#'
    elif sx - ex == 0:
        for y in range(min(sy, ey), max(sy, ey) + 1):
            m[y][ex] = '#'

def get_bounds(m, y_max=None) -> int:
    x_min, x_max = len(m[0]), 0
    y_max = len(m) if y_max is None else y_max

    for x in range(len(m[0])):
        for y in range(y_max):
            x_min = x if m[y][x] != '.' and x < x_min else x_min
            x_max = x if m[y][x] != '.' and x > x_max else x_max

    return x_min, x_max 

def generate_map(scan: ScanDataType, origin) -> MapType:
    _, max_d = get_dimensions(scan)

    max_d = max_d[0] * 2, max_d[1]

    m = [['.' for _ in range(max_d[0] + 1)] for _ in range(max_d[1] + 1)]

    for path in scan:
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            draw_wall(m, start, end)
    
    m[origin[1]][origin[0]] = '+'

    return m

def print_map(m: MapType, origin=(500, 0), bounds=None, part_two=False):
    lm, rm = bounds if bounds else get_bounds(m, len(m) - 1 if part_two else None)
    rm += 1

    width = 4
    x_labels = list(map(lambda x: (f'{x:>4}', x), [lm, origin[0], rm - 1]))

    for i in range(width):
        s = [' '] * (len(m[0][lm:rm]) + 1)

        for label in x_labels:
            l, pos = label
            s_idx = pos - lm
            s[s_idx] = l[i]

        print(f"{' ' * width}{''.join(s)}")

    for i, line in enumerate(m):
        print(f"{i:<4}{''.join(line[lm:rm])}")

def step(m, pos: PointType):
    x, y = pos

    if y + 1 == len(m):
        return (-1, -1)

    below = m[y + 1][x]

    if below == '#' or below == 'o':
        if x - 1 >= 0:
            left = m[y + 1][x - 1]
            if left != '#' and left != 'o':
                return x - 1, y + 1


        right = m[y + 1][x + 1]
        if right != '#' and right != 'o':
            return x + 1, y + 1

        return x, y

    return x, y + 1

def run(m: MapType, origin):
    spawn_count = 0

    while True:
        spawn_count += 1
        path = []
        prev = origin
        
        while pos := step(m, prev):
            # out of bounds (drops off into abyss)
            if pos == (-1, -1):
                for pt in path:
                    m[pt[1]][pt[0]] = '~'

                return spawn_count - 1

            if pos == prev:
                m[pos[1]][pos[0]] = 'o'
                # print_map(m)
                break

            path.append(pos)
            prev = pos

        # nothing spawned or stable origin spawn
        if (len(path) == 0 or pos == origin):
            return spawn_count 

def part_one(data: list[str]) -> int:
    scan = parse_scan(data)

    origin = (500, 0)
    m = generate_map(scan, origin)

    #print_map(m)

    spawn_count = run(m, origin)

    #print_map(m)

    return spawn_count


def part_two(data: list[str]) -> int:
    scan = parse_scan(data)

    origin = (500, 0)
    m = generate_map(scan, origin)

    # add floor
    m.append(['.' for _ in range(len(m[0]))])
    m.append(['#' for _ in range(len(m[0]))])

    #print_map(m, part_two=True)

    spawn_count = run(m, origin)

    #print_map(m, part_two=True)

    return spawn_count


def main():
    print('Day 14: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day14_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day14', '\n'))))
    print('Day 14: Answer for Part 2: {}'.format(
        #part_two(read_input('../tests/inputs/test_input_day14_1.txt', '\n'))))
        part_two(read_input('../inputs/input_day14', '\n'))))


if __name__ == "__main__":
    main()
