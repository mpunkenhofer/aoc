from src.common.util import read_input


def part_one(data: list[str]) -> int:
    max_subtotal = 0
    subtotal = 0

    for d in data:
        if d == '':
            max_subtotal = subtotal if subtotal > max_subtotal else max_subtotal
            subtotal = 0
        else:
            subtotal += int(d)

    return max_subtotal


def part_two(data: list[str]) -> int:
    totals: list[int] = []
    subtotal: int = 0

    for d in data:
        if d == '':
            totals.append(subtotal)
            subtotal = 0
        else:
            subtotal += int(d)

    totals = sorted(totals)

    print(totals[-3:])

    return sum(totals[-3:])


def main():
    print('Day 01: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day01', '\n'))))
    print('Day 01: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day01', '\n'))))


if __name__ == "__main__":
    main()
