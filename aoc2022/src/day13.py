from src.common.util import read_input
import json

def parse_lists(data: list[str]):
    lists = []

    for line in data:
        if line:
            lists.append(json.loads(line))
    
    return lists

def compare_lists(left, right, log=print):
    return compare(left, right, log) == 1

def compare(left, right, log) -> int:
    c = lambda l, r: compare(l, r, log)    
    log(f'- Compare {left} vs {right}')


    leftType = 'list' if isinstance(left, list) else 'int'
    rightType = 'list' if isinstance(right, list) else 'int'

    # convert to list if exactly one value is an integer and retry
    if leftType == 'int' and rightType == 'list':
        log(f'- Mixed types; convert left to [{left}] and retry comparison.')
        return c([left], right)
    if rightType == 'int' and leftType == 'list':
        log(f'- Mixed types; convert right to [{right}] and retry comparison.')
        return c(left, [right])

    # both are int - perform comparison
    if 'int' == leftType == rightType:
        if left == right:
            return 0
        elif left < right:
            log('- Left side is smaller, so inputs are in the right order.')
            return 1
        else:
            log('- Right side is smaller, so inputs are not in the right order.')
            return -1

    # both are lists - pop one
    if len(left) == 0:
        log('- Left side ran out of items, so inputs are in the right order.')
        return 1
    if len(right) == 0:
        log('- Right side ran out of items, so inputs are not in the right order.')
        return -1

    l = left.pop(0)
    r = right.pop(0)
        
    result = c(l, r)

    if result != 0:
        return result
    elif len(left) == len(right) == 0:
        return 0
    else:
        return c(left, right)

def part_one(data: list[str]) -> int:
    no_print = lambda _: _
    lists = parse_lists(data)
    correct = []

    for i in range(0, len(lists), 2):
        idx = int(i / 2 + 1)
        #print(f'== Pair {idx} ==')
        if compare_lists(lists[i], lists[i + 1], no_print):
            correct.append(idx)

    print(correct)

    return sum(correct)


def part_two(data: list[str]) -> int:
    lists = parse_lists(data)

    return 0


def main():
    print('Day 13: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day13_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day13', '\n'))))
    print('Day 13: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day13', '\n'))))


if __name__ == "__main__":
    main()
