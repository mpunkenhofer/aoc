from src.common.util import read_input


def calculate_loop_size(pub_key):
    loop_size = 0
    value = 1

    while value != pub_key:
        value *= 7
        value %= 20201227
        loop_size += 1

    return loop_size

def calculate_encryption_key(pub_key, loop_size):
    pk = 1

    for _ in range(loop_size):
        pk *= pub_key
        pk %= 20201227

    return pk

def part_one(input):
    pub_keys = [int(k) for k in input]
    loop_sizes = [calculate_loop_size(k) for k in pub_keys]
    pks = [calculate_encryption_key(k, lsz) for k, lsz in zip(pub_keys, loop_sizes[::-1])]

    return pks[0]


def part_two(input):
    return 0


def main():
    print('Day 25: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day25.txt', '\n'))))
    print('Day 25: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day25.txt', '\n'))))


if __name__ == "__main__":
    main()
