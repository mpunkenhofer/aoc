from typing import List
from src.common.util import read_input
import re

def part_one(data: list[str]) -> int: 
    sum = 0

    for line in data:
        digits = ''.join(re.findall(r'\d+', line))

        if digits:
            sum += int(digits[0] + digits[-1])

    return sum


def left_most_digit(line: str, digits: List[str]) -> str:
    i = 0

    while i < len(line):
        k = i
        if line[k].isdigit():
            return line[k]

        for d_idx, digit in enumerate(digits):
            j = 0
            k = i
            while j < len(digit):
                if line[k] != digit[j]:
                    break
                else:
                    k += 1
                    j += 1

            if j == len(digit):
                return str(d_idx)

        i += 1

    return None

def part_two(data: list[str]) -> int:
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    rdigits = [digit[::-1] for digit in digits]

    sum = 0

    for line in data:
        number = int(left_most_digit(line, digits) + left_most_digit(line[::-1], rdigits))
        sum += number

    return sum


def main():
    print('Day 01: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day01', '\n'))))
    print('Day 01: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day01', '\n'))))


if __name__ == "__main__":
    main()
