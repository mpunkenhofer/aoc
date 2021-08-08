from src.common.util import read_input


def parse_answers(input):
    groups = []

    current_group = set()

    for line in input:
        if not line:
            groups.append(current_group)
            current_group = set()
            continue
        current_group |= set(line)
    return groups

def part_one(input):
    return sum(map(len, parse_answers(input)))


def part_two(input):
    sum = 0
    current_group_answers = []

    for line in input:
        if not line and current_group_answers:
            same_answers = set.intersection(*current_group_answers)
            sum += len(same_answers)
            current_group_answers = []
            continue

        current_group_answers.append(set(line))

    return sum


def main():
    print('Day 6: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day6.txt', '\n'))))
    print('Day 6: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day6.txt', '\n'))))


if __name__ == "__main__":
    main()
