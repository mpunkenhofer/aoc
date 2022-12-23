from typing import Tuple
from src.common.util import read_input

def eval_prog(lines: list[str]) -> list[Tuple[int, int]]:
    register_values = [(1, 0)]
    cycle = 1

    for line in lines:
        values = line.split()

        if (len(values) == 2):
            op, v = values[0], int(values[1])

            if op == "addx":
                cycle += 2
                register_values.append((register_values[-1][0] + v, cycle))
        else:
            cycle += 1
    
    return register_values

def analyze_prog(lines: list[str], base=20, inc=40) -> int:
    x_values = eval_prog(lines)

    result = []
    current = base
    prev = 0 

    for x, c  in x_values:
        if c > current:
            result.append(prev * current)
            current += inc
        prev = x
            
    return sum(result)

def render(values: list[Tuple[int, int]], width=40, height=6, sprite_size=3):
    values = values[1:]
    screen = [['.' for _ in range(width)] for _ in range(height)]

    sprite_pos = 0
    i = 0

    for y in range(height):
        for x in range(width):
            value = values[i] if i < len(values) else (sprite_pos + 1, 0)
            cycle = y * width + x + 1

            if cycle >= value[1]:
                sprite_pos = value[0] - 1
                i += 1

            if sprite_pos <= x < sprite_pos + sprite_size:
                screen[y][x] = '#'

            
    for line in screen:
        print(''.join(line))

def part_one(data: list[str]) -> int:
    return analyze_prog(data)


def part_two(data: list[str]) -> int:
    render(eval_prog(data))
    return 0


def main():
    print('Day 10: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day10_2.txt', '\n'))))
        part_one(read_input('../inputs/input_day10', '\n'))))
    print('Day 10: Answer for Part 2: {}'.format(
        #part_two(read_input('../tests/inputs/test_input_day10_2.txt', '\n'))))
        part_two(read_input('../inputs/input_day10', '\n'))))


if __name__ == "__main__":
    main()
