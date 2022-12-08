from src.common.util import read_input
import numpy as np


def read_map(data: list[str]) -> np.ndarray:
    map: list[list[int]] = []

    for line in data:
        l = []
        for char in line:
            l.append(int(char))

        map.append(l)

    return np.array(map)


def trees_visible(map: np.ndarray) -> int:
    count = 0

    for y in range(1, len(map) - 1):
        for x in range(1, len(map[y]) - 1):
            current = map[y, x]
            def f(x): return x < current
            top = np.all(f(map[0:y, x]))
            bot = np.all(f(map[y+1:, x]))
            left = np.all(f(map[y, 0:x]))
            right = np.all(f(map[y, x+1:]))

            if (top or bot or left or right):
                count += 1

    edge = 4 * len(map) - 4
    return edge + count


def part_one(data: list[str]) -> int:
    map = read_map(data)

    return trees_visible(map)


def visibility(a: np.ndarray, current: int) -> int:
    count, i = 0, 0

    while i < a.size:
        c = a[i]

        i += 1
        count += 1

        if c >= current:
            break

    return count


def calc_scenic_score(map: np.ndarray) -> np.ndarray:
    result = np.zeros(map.shape)

    for y in range(1, len(map) - 1):
        for x in range(1, len(map[y]) - 1):
            current = map[y, x]

            top = visibility(np.flip(map[0:y, x]), current)
            bot = visibility(map[y+1:, x], current)
            left = visibility(np.flip(map[y, 0:x]), current)
            right = visibility(map[y, x+1:], current)

            if (top or bot or left or right):
                result[y, x] = top * bot * left * right

    return result


def part_two(data: list[str]) -> int:
    map = read_map(data)

    scores = calc_scenic_score(map)
    return int(np.amax(scores))


def main():
    print('Day 08: Answer for Part 1: {}'.format(
        # part_one(read_input('../tests/inputs/test_input_day08_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day08', '\n'))))
    print('Day 08: Answer for Part 2: {}'.format(
        # part_two(read_input('../tests/inputs/test_input_day08_1.txt', '\n'))))
        part_two(read_input('../inputs/input_day08', '\n'))))


if __name__ == "__main__":
    main()
