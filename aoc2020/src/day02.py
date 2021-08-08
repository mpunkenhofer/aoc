from src.common.util import read_input


def input_to_list(input):
    password_infos = []

    for line in input:
        r, l, p = line.split(' ')
        r = r.split('-')
        password_infos.append(((int(r[0]), int(r[1])), l[0], p))

    return password_infos


def is_valid_part_one(password_info):
    (r_start, r_end), letter, password = password_info
    return r_start <= password.count(letter) <= r_end


def is_valid_part_two(password_info):
    (p1, p2), letter, password = password_info
    password_len = len(password)

    return (p1 < password_len and password[p1 - 1] == letter) ^ (p2 < password_len and password[p2 - 1] == letter)


def part_one(input):
    password_infos = input_to_list(input)
    return sum(map(is_valid_part_one, password_infos))


def part_two(input):
    password_infos = input_to_list(input)
    return sum(map(is_valid_part_two, password_infos))


def main():
    print('Day 2: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day2.txt', '\n'))))
    print('Day 2: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day2.txt', '\n'))))


if __name__ == "__main__":
    main()
