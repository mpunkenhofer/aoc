from src.common.util import read_input
import re

def parse_bags(input):
    bags = {}

    for line in input:
        if not line:
            continue

        rule, contents = line.split('contain')
        contents = contents.split(',')

        rule_contents = []

        for c in contents:
            match = re.match(r'(\d+)\s(.+)\s(bag|bags)', c.strip())
            if match:
                count = int(match.group(1))
                bag_type = match.group(2)
                rule_contents.append((count, bag_type))
        
        match = re.match(r'(.+)\s(bag|bags)', rule.strip())
        if match:
            bags[match.group(1)] = rule_contents

    return bags


def in_contents(contents, *colors):
    for _, color in contents:
        for c in colors:
            if color == c:
                return True
    return False

def get_bag_count(bags, color):
    for bag in bags:
        pass

def part_one(input):
    bags = parse_bags(input)

    result = []
    queue = ['shiny gold']

    while queue:
        current = queue.pop(0)

        if current in result:
            continue
        else:
            result.append(current)

        for b, contents in bags.items():
            if in_contents(contents, current):
                queue.append(b)


    return len(result) - 1


def bag_carry_requirement(bags, target):
    total = 1

    for bag in bags[target]:
        cnt, color = bag
        total += cnt * bag_carry_requirement(bags, color)

    return total

def part_two(input):
    bags = parse_bags(input)

    return bag_carry_requirement(bags, 'shiny gold') - 1 


def main():
    print('Day 7: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day7.txt', '\n'))))
    print('Day 7: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day7.txt', '\n'))))


if __name__ == "__main__":
    main()
