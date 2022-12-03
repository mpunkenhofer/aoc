from src.common.util import read_input


def get_priority(letter: str) -> int:
    priority = ord(letter.lower()) - 96
    priority += 26 if letter[0].isupper() else 0

    return priority


def part_one(data: list[str]) -> int:
    priorities: int = 0

    for line in data:
        half = int(len(line) / 2)
        a, b = line[:half], line[half:]

        set_a, set_b = set(a), set(b)
        ab = set_a.intersection(set_b)

        shared_letter = next(iter(ab))

        priorities += get_priority(shared_letter)

    return priorities


def part_two(data: list[str]) -> int:
    priorities: int = 0

    for i in range(0, len(data), 3):
        a = data[i]
        b = data[i + 1]
        c = data[i + 2]
        abc = set(a).intersection(set(b).intersection(set(c)))

        shared_letter = next(iter(abc))

        priorities += get_priority(shared_letter)

    return priorities


def main():
    print('Day 03: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day03', '\n'))))
    print('Day 03: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day03', '\n'))))


if __name__ == "__main__":
    main()
