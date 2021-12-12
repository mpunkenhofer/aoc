from common.util import read_input
import numpy as np

class LineSegment:
    def __init__(self, string) -> None:
        start, stop = string.split('->')
        self.x1, self.y1 = tuple(map(int, start.split(',')))
        self.x2, self.y2 = tuple(map(int, stop.split(',')))
    
    def line_coordinates(self, horizontal_only=True):
        coords = []

        if horizontal_only and not (self.x1 == self.x2 or self.y1 == self.y2):
            return []

        x, y = self.x1, self.y1

        while x != self.x2 or y != self.y2:
            coords.append([x, y])

            if x != self.x2:
                x += 1 if self.x1 < self.x2 else -1
            if y != self.y2:
                y += 1 if self.y1 < self.y2 else -1

        coords.append([x, y])

        return coords

def init_line_segments(data):
    ls = []

    for row in data:
        ls.append(LineSegment(row))
    
    return ls

def part_one(data, horizontal_only=True):
    line_segments = init_line_segments(data)
    lines = []
    max_coord = 0

    for ls in line_segments:
        line = ls.line_coordinates(horizontal_only)
        lines.append(line)

        for p in line:
            if p[0] > max_coord:
                max_coord = p[0]
            if p[1] > max_coord:
                max_coord = p[1]

    diag = np.zeros((max_coord + 1, max_coord + 1))

    for line in lines:
        for p in line:
            diag[p[1], p[0]] += 1

    return np.count_nonzero(diag > 1)


def part_two(data):
    return part_one(data, False)


def main():
    # print('Day 05: Answer for Test 1: {}'.format(
    #     part_two(read_input('inputs/test_input_day05_1.txt', '\n'))))

    print('Day 05: Answer for Part 1: {}'.format(
        part_one(read_input('inputs/input_day05.txt', '\n'))))
    print('Day 05: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day05.txt', '\n'))))


if __name__ == "__main__":
    main()
