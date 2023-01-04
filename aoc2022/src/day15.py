from typing import Tuple
from src.common.util import read_input
import re
import numpy as np
import sys

PointType = Tuple[int, int]
SensorDataType = Tuple[PointType, PointType, int]
SensorDataList = list[SensorDataType]

def parse_sensor_data(data: list[str]) -> SensorDataList:
    result = []
    regex = r'x=(-?\d+), y=(-?\d+)'

    for line in data:
        sensor, beacon = line.split(':')
        sensor = tuple(map(int, re.search(regex, sensor).groups()))
        beacon = tuple(map(int, re.search(regex, beacon).groups()))
        distance = manhatten_distance(sensor, beacon)

        result.append((sensor, beacon, distance))

    return result

def bounds(l: SensorDataList):
    x0, y0 = l[0][0]
    x1, y1 = l[0][0]

    for pair in l:
        sensor, beacon, _ = pair
        x0 = min(beacon[0], min(sensor[0], x0))
        y0 = min(beacon[1], min(sensor[1], y0))
        x1 = max(beacon[0], max(sensor[0], x1))
        y1 = max(beacon[1], max(sensor[1], y1))

    return (x0, y0), (x1, y1)

def manhatten_distance(p0: PointType, p1: PointType):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

def draw_sensor_map(l: SensorDataList, p0: PointType, p1: PointType, covered=[]):
    sensors = [s[0] for s in l]
    beacons = [s[1] for s in l]

    width = p1[0] - p0[0]

    x_label_width = max(4, len(str(p1[0])) + 1)
    y_label_width = max(3, len(str(p1[1])) + 1)

    # labels for x axis
    x_shift = 0 if p0[0] > 0 else -p0[0]
    x_labels = list(map(lambda x: (f'{x:>{x_label_width}}', x), range(0, p1[0] + 1, 5)))

    for i in range(x_label_width):
        s = [' '] * (width)

        for l, pos in x_labels:
            s[pos] = l[i]

        print(f"{' ' * (y_label_width + x_shift)}{''.join(s)}")

    # draw map incl y axis labels
    for y in range(p0[1], p1[1] + 1):
        s = f'{y:<{y_label_width}}'
        for x in range(p0[0], p1[0] + 1):
            if (x, y) in sensors:
                s += 'S'
            elif (x, y) in beacons:
                s += 'B'
            elif (x, y) in covered:
                s += '#'
            else:
                s += '.'
        print(s)

def progress_bar(value, end_value, bar_length=20):
    percent = float(value) / end_value
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

# Brute force approach 1
# def get_covered(l: SensorDataList, y):
#     covered = set()
#     p0, p1 = bounds(l)

#     width = p1[0] - p0[0]
#     x_shift = 0 if p0[0] > 0 else -p0[0]

#     for x in range(p0[0], p1[0] + 1):
#         progress_bar(x + x_shift, width)
#         for s, b, d in l:
#             if s == (x, y) or b == (x, y):
#                 continue

#             sd = manhatten_distance((x, y), s)

#             if sd <= d:
#                 covered.add([x, y])
    
#     return covered

def merge_intervals(intervals):
    if (len(intervals) < 1):
        return []

    result = []

    intervals = sorted(intervals, key=lambda i: min(i[0], i[1]))

    result.append(intervals[0])

    for current in intervals[1:]:
        cs, ce = current

        if cs <= result[-1][1]:
            result[-1][1] = max(ce, result[-1][1])
        else:
            result.append(current)

    return result

def coverage(l: SensorDataList, y):
    intervals = []

    for sensor, _, d in l:
        sx, sy = sensor

        if sy - d <= y <= sy + d:
            yd = abs(y - sy)
            xd = abs(d - yd)

            intervals.append([sx - xd , sx + xd])

    return merge_intervals(intervals)

def to_coordinates(intervals, y):
    coords = []

    for current in intervals:
        for x in range(current[0], current[1] + 1):
            coords.append((x, y))

    return coords


def calc_impossible_locs(l: SensorDataList, y: int) -> int:
    intervals = coverage(l, y)

    locs = 0

    for current in intervals:
        d = abs(current[1] - current[0]) + 1
        locs += d
    
    same_y = set()

    for s, b, _ in l:
        if s[1] == y:
            same_y.add(s[0])
        if b[1] == y:
            same_y.add(b[0])

    return locs - len(same_y)

def part_one(data: list[str], y=2000000) -> int:
    sensor_list = parse_sensor_data(data)

    # test case - do a bit more
    if (y == 10):
        covered = []

        for yi in range(9, 12):
            covered += to_coordinates(coverage(sensor_list, yi), yi)
        
        draw_sensor_map(sensor_list, (-4, 9), (26, 11), covered)

    return calc_impossible_locs(sensor_list, y)


def calculate_coordinates(l, limit):
    for y in range(limit, -1, -1):
        #progress_bar(y, limit)
        intervals = coverage(l, y)
        
        if len(intervals) > 1:
            #progress_bar(limit, limit)
            #print()
            return intervals[0][1] + 1, y

    return 0, 0

def part_two(data: list[str], limit=4000000) -> int:
    sensor_list = parse_sensor_data(data)

    x, y = calculate_coordinates(sensor_list, limit)

    print(f'distress beacon coordinates: x = {x}, y = {y}.')

    return 4000000 * x + y


def main():
    print('Day 15: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day15_1.txt', '\n'), 10)))
        part_one(read_input('../inputs/input_day15', '\n'))))
    print('Day 15: Answer for Part 2: {}'.format(
        #part_two(read_input('../tests/inputs/test_input_day15_1.txt', '\n'), 20)))
        part_two(read_input('../inputs/input_day15', '\n'))))


if __name__ == "__main__":
    main()
