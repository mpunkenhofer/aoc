from common.util import read_input
import numpy as np

def part_one(data):
    data = np.array(data, dtype=int)

    inc = 0

    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            inc += 1

    return inc


def part_two(data):
    data = np.array(data, dtype=int)

    window_size, prev, inc = 3, -1, 0
    for i in range(window_size - 1, len(data)):
        s = 0

        for j in range(window_size):
            s += data[i - j]

        if s > prev and prev > 0:
            inc += 1
        
        prev = s

    return inc


def main():
    print('Day 1: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day01.txt', '\n'))))

    print('Day 1: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day01.txt', '\n'))))


if __name__ == "__main__":
    main()
