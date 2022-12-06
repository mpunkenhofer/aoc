from src.common.util import read_input


def find_marker(data_stream, length):
    for i in range(len(data_stream)):
        marker = data_stream[i:i+length]
        s_marker = set(marker)

        if len(s_marker) == length:
            return i+length

    return -1


def part_one(data: list[str]) -> int:
    return find_marker(data[0], 4)


def part_two(data: list[str]) -> int:
    return find_marker(data[0], 14)


def main():
    print('Day 06: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day06', '\n'))))
    print('Day 06: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day06', '\n'))))


if __name__ == "__main__":
    main()
