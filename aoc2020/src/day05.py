from src.common.util import read_input
import math

def scan_boarding_pass(boarding_pass):
    row_lower, row_upper = 0, 127

    for c in boarding_pass[:7]:
        if c == 'F':
            row_upper = row_lower + math.floor((row_upper - row_lower) / 2)
        elif c == 'B':
            row_lower = row_lower +  math.ceil((row_upper - row_lower) / 2)
    
    col_lower, col_upper = 0, 7

    for c in boarding_pass[-3:]:
        if c == 'L':
            col_upper = col_lower + math.floor((col_upper - col_lower) / 2)
        elif c == 'R':
            col_lower = col_lower +  math.ceil((col_upper - col_lower) / 2)

    row = row_lower
    col = col_lower
    sead_id = row * 8 + col

    return (row, col, sead_id)

def part_one(input):
    max = 0

    for boarding_pass in input:
        (_, _, id) = scan_boarding_pass(boarding_pass)
        if id > max:
            max = id

    return max


def part_two(input):
    boarding_passes = sorted([scan_boarding_pass(bp) for bp in input], key=lambda x: x[-1])

    for i, boarding_pass in enumerate(boarding_passes[:-1]):
        seat_id_delta = abs(boarding_pass[-1] - boarding_passes[i + 1][-1])
        if seat_id_delta > 1:
            return (boarding_pass[-1] + 1)

    return 0

def main():
    print('Day 5: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day5.txt', '\n'))))
    print('Day 5: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day5.txt', '\n'))))


if __name__ == "__main__":
    main()
