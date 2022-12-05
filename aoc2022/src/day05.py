import re
from typing import Tuple
from src.common.util import read_input


def print_stacks(stacks: list[list[str]]):
    max_size = max(map(len, stacks))

    for j in range(max_size):
        out = ''
        for i in range(len(stacks)):
            if j < len(stacks[i]):
                crate = stacks[i][j]
            else:
                crate = ''

            out += f'{crate:>3} '

        print(out)


def get_top(stacks: list[list[str]]):
    top = ''

    for stack in stacks:
        top += stack[0]

    return re.sub(r'\[|\]', '', top)


def parse_input(data: list[str]):
    parsed_stacks: list[list[str]] = []
    moves: list[(int, int, int)] = []

    it = iter(data)
    while (line := next(it, None)) is not None and line != '':
        result = list(
            map(lambda s: s.strip(), re.findall(r'\[\w\]\s?|\s{3}\s?', line)))
        parsed_stacks.append(result)

    while (line := next(it, None)) is not None:
        result = list(map(int, re.findall(r'\d+', line)))
        moves.append(result)

    # discard last line (stack enumeration)
    parsed_stacks = parsed_stacks[:-1]

    stacks: list[list[str]] = [[] for _ in range(len(parsed_stacks[0]))]

    for i in range(len(parsed_stacks)):
        for j in range(len(parsed_stacks[i])):
            crate = parsed_stacks[i][j]
            if (crate != ''):
                stacks[j].append(crate)

    return stacks, moves


def move_crates(stacks: list[list[str]], move: Tuple[int, int, int], version=9000):
    quantity, source, target = move

    source -= 1
    target -= 1

    crates = stacks[source][:quantity]
    stacks[source] = stacks[source][quantity:]

    if version == 9000:
        stacks[target] = crates[::-1] + stacks[target]
    else:
        stacks[target] = crates + stacks[target]

    return stacks


def part_one(data: list[str]) -> int:
    stacks, moves = parse_input(data)

    print_stacks(stacks)

    for move in moves:
        stacks = move_crates(stacks, move)

    print_stacks(stacks)

    return get_top(stacks)


def part_two(data: list[str]) -> int:
    stacks, moves = parse_input(data)

    print_stacks(stacks)

    for move in moves:
        stacks = move_crates(stacks, move, 9001)

    print_stacks(stacks)

    return get_top(stacks)


def main():
    print('Day 05: Answer for Part 1: {}'.format(
        # part_one(read_input('../tests/inputs/test_input_day05_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day05', '\n'))))
    print('Day 05: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day05', '\n'))))


if __name__ == "__main__":
    main()
