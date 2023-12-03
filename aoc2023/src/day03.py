from src.common.util import read_input


def parse_number(line: str, idx: int) -> int:
    b = e = idx

    while b >= 0 and line[b].isdigit():
        b -= 1
    
    while e < len(line) and line[e].isdigit():
        e += 1
    
    b += 1

    number = line[b:e]

    return number, b, e

def part_one(data: list[str]) -> int:
    sum = 0

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c.isdigit() or c == '.':
                continue
            else:
                wy = max(0, y - 1)
                while wy < min(len(data), y + 2):
                    wx = max(0, x - 1)
                    while wx < min(len(data[wy]), x + 2):
                        number = ''

                        if data[wy][wx].isdigit():
                            number, _, e = parse_number(data[wy], wx)

                            sum += int(number) if len(number) > 0 else 0 

                        wx = e if len(number) > 0 else wx + 1

                    wy += 1
    return sum


def part_two(data: list[str]) -> int:
    gear_ratios = 0

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '*':
                numbers = []

                wy = max(0, y - 1)
                while wy < min(len(data), y + 2):
                    wx = max(0, x - 1)
                    while wx < min(len(data[wy]), x + 2):
                        number = ''

                        if data[wy][wx].isdigit():
                            number, b, e = parse_number(data[wy], wx)

                            numbers.append(int(number))

                        wx = e if len(number) > 0 else wx + 1

                    wy += 1
                
                if len(numbers) == 2:
                    gear_ratios += numbers[0] * numbers[1]

    return gear_ratios


def main():
    print('Day 03: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day03', '\n'))))
    print('Day 03: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day03', '\n'))))


if __name__ == "__main__":
    main()
