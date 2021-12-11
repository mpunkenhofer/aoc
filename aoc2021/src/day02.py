from typing import List
from common.util import read_input


def part_one(data: List[str]):
    position = depth = 0

    for d in data:
        direction, units = d.split()
        units = int(units)

        if direction == 'forward':
            position += units
        elif direction == 'down':
            depth += units
        elif direction == 'up':
            depth -= units

    return depth * position


def part_two(data):
    position = depth = aim = 0

    for d in data:
        direction, units = d.split()
        units = int(units)

        if direction == 'forward':
            position += units
            depth += aim * units
        elif direction == 'down':
            aim += units
        elif direction == 'up':
            aim -= units

    return depth * position

def main():
    print('Day 1: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day02.txt', '\n'))))
    print('Day 1: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day02.txt', '\n'))))


if __name__ == "__main__":
    main()
