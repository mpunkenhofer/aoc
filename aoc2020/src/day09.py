from src.common.util import read_input
from itertools import combinations


def find_invalid_number(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if numbers[i] not in map(sum, combinations(numbers[i - preamble:i], 2)):
            return numbers[i]

    return 0


def find_subarray_sequence(numbers, invalid_number):
    result = []
    current_sum = 0

    for n in numbers:
        current_sum += n

        while current_sum > invalid_number:
            current_sum -= result.pop(0)

        if current_sum == invalid_number:
            return result

        result.append(n)

    return result

def part_one(input, preamble=25):
    numbers = [int(i) for i in input if i]

    return find_invalid_number(numbers, preamble)


def part_two(input, preamble=25):
    numbers = [int(i) for i in input if i]

    invalid_number = find_invalid_number(numbers, preamble)
    subarray = find_subarray_sequence(numbers, invalid_number)
    return min(subarray) + max(subarray)


def main():
    print('Day 9: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day9.txt', '\n'))))
    print('Day 9: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day9.txt', '\n'))))


if __name__ == "__main__":
    main()
