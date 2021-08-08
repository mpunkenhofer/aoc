from src.common.util import read_input


def check_slope(slope, right, down):
    r = 0
    d = 0
    trees = 0

    while d < len(slope):
        if slope[d][r % len(slope[d])] == '#':
            trees += 1
        r += right
        d += down

    return trees


def part_one(input):
    return check_slope(input, 3, 1)


def part_two(input):
    s1 = check_slope(input, 1, 1)
    s2 = check_slope(input, 3, 1)
    s3 = check_slope(input, 5, 1)
    s4 = check_slope(input, 7, 1)
    s5 = check_slope(input, 1, 2)

    return s1 * s2 * s3 * s4 * s5


def main():
    print('Day 3: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day3.txt', '\n'))))
    print('Day 3: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day3.txt', '\n'))))


if __name__ == "__main__":
    main()
