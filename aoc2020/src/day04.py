from src.common.util import read_input
import re

def parse_passports(input):
    passports = []
    current_passport = {}

    for line in input:
        if not line:
            if current_passport:
                passports.append(current_passport)
            current_passport = {}
            continue

        fields = line.split(' ')

        for field in fields:
            key, value = field.split(':')
            current_passport[key] = value

    return passports


def validate_fields(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = passport.keys() >= required_fields
    return valid


def validate_values(passport):
    try:
        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt: str = passport['hgt']
        hcl: str = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']

        if not 1920 <= byr <= 2002:
            return False

        if not 2010 <= iyr <= 2020:
            return False

        if not 2020 <= eyr <= 2030:
            return False
        
        if hgt.endswith('cm'):
            cm = int(hgt.split('cm')[0])
            if not 150 <= cm <= 193:
                return False
        elif hgt.endswith('in'):
            inch = int(hgt.split('in')[0])
            if not 59 <= inch <= 76:
                return False
        else:
            return False

        if re.match('#([a-f]|[0-9]){6}', hcl) is None:
            return False

        if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        
        if len(pid) != 9 or not all(c.isdigit() for c in pid):
            return False

        return True
    except KeyError:
        return False

def part_one(input):
    return sum(map(validate_fields, parse_passports(input)))


def part_two(input):
    return sum(map(validate_values, parse_passports(input)))


def main():
    # print('Day 4: Answer for Part 1 {}'.format(
    #     part_one(read_input('inputs/reddit_day4_input_help.txt', '\n'))))
    print('Day 4: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day4.txt', '\n'))))
    print('Day 4: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day4.txt', '\n'))))


if __name__ == "__main__":
    main()
