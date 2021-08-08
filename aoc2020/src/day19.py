import re 
from src.common.util import read_input
from itertools import chain

def parse_input(input):
    rules, messages = {}, []

    for line in input:
        rule_match = re.match(r'\d+:', line)

        if rule_match:
            rule_nr, rule_content = line.split(':')

            rule_nr = int(rule_nr)

            char_match = re.match(r'"([a-z])"', rule_content.strip())

            if char_match:
                rules[rule_nr] = char_match.group(1)
            else:
                rules[rule_nr] = [[int(i) for i in s.strip().split(' ')] for s in rule_content.split('|')]
        else:
            if line:
                messages.append(line)

    return rules, messages

def verify(messages, rules):
    def verify_helper(rule_stack, current=''):
        valid_messages = 0

        while rule_stack:
            rule = rule_stack.pop(0)
            if isinstance(rule, str):
                current += rule
            elif isinstance(rule, list):
                top_rule = rule[0]

                for r in rule[1:]:
                    valid_messages += verify_helper(list(r + rule_stack), current)

                rule_stack = top_rule + rule_stack
            else:
                rule_stack = [rules[rule]] + rule_stack

        if current in messages:
            valid_messages += 1
        
        return valid_messages

    return verify_helper(list(chain(*rules[0])))

def part_one(input):
    rules, messages = parse_input(input)

    return verify(messages, rules)

def part_two(input):
    rules, messages = parse_input(input)

    # modify certain rules
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    
    return 0


def main():
    print('Day 19: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day19.txt', '\n'))))
    print('Day 19: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day19.txt', '\n'))))


if __name__ == "__main__":
    main()
