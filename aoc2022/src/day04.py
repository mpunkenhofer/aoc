import math
from src.common.util import read_input


def part_one(data: list[str]) -> int:
    overlap_cnt: int = 0

    for line in data:
        sections = line.split(',')
        s1 = list(map(int, sections[0].split('-')))
        s2 = list(map(int, sections[1].split('-')))

        s1_delta = s1[1] - s1[0]
        s2_delta = s2[1] - s2[0]

        a = s1 if s1_delta > s2_delta else s2
        b = s2 if s1_delta > s2_delta else s1

        if (b[0] >= a[0] and b[1] <= a[1]):
            overlap_cnt += 1

    return overlap_cnt


def check_overlap(i1, i2):
    return i2[0] >= i1[0] and i2[0] <= i1[1]


def part_two(data: list[str]) -> int:
    overlap_cnt: int = 0

    for line in data:
        sections = line.split(',')
        s1 = list(map(int, sections[0].split('-')))
        s2 = list(map(int, sections[1].split('-')))

        if (check_overlap(s1, s2) or check_overlap(s2, s1)):
            overlap_cnt += 1

    return overlap_cnt


def main():
    print('Day 04: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day04', '\n'))))
    print('Day 04: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day04', '\n'))))


if __name__ == "__main__":
    main()
