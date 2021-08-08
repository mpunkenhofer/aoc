from src.common.util import read_input


def part_one(input):
    expenses_report = [int(i) for i in input]
    n = len(expenses_report)

    for i in range(n):
        for j in range(i + 1, n):
            if expenses_report[i] + expenses_report[j] == 2020:
                return expenses_report[i] * expenses_report[j]

    return 0


def part_two(input):
    expenses_report = [int(i) for i in input]
    n = len(expenses_report)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if expenses_report[i] + expenses_report[j] + expenses_report[k] == 2020:
                    return expenses_report[i] * expenses_report[j] * expenses_report[k]

    return 0


def main():
    print('Day 1: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/day1/input', '\n'))))
    print('Day 1: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/day1/input', '\n'))))


if __name__ == "__main__":
    main()
