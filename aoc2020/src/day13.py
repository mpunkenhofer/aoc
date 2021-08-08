import numpy as np
from src.common.util import read_input
from functools import reduce

def part_one(input):
    timestamp, bus_ids = int(input[0]), [int(id) for id in filter(lambda x: x != 'x', input[1].split(','))]

    depatures = [(timestamp - (timestamp % id) + id, id) for id in bus_ids]
    earliest = sorted(depatures)[0]

    return (abs(timestamp - earliest[0])) * earliest[1]


def chinese_remainder(congruences):
    prod = lambda x, y: x * y
    N = reduce(prod, map(lambda x: x[1], congruences))
    n = []

    for i, ci in enumerate(congruences):
        ai = ci[0]
        ni = reduce(prod, map(lambda x: x[1], congruences[:i] + congruences[i+1:]))
        xi = pow(ni, -1, ci[1])
        n.append(ai * ni * xi)

    return sum(n) % N

def part_two(input):
    bus_ids = [int(id) if id != 'x' else 0 for id in input[1].split(',')]

    congruences = list(filter(lambda id: id[1] != 0, zip(range(len(bus_ids))[::-1], bus_ids)))

    return chinese_remainder(congruences) - len(bus_ids) + 1


def main():
    print('Day 13: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day13.txt', '\n'))))
    print('Day 13: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day13.txt', '\n'))))


if __name__ == "__main__":
    main()
