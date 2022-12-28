from src.common.util import read_input
import re

class Monkey:
    def __init__(self, items, expr, test) -> None:
        self.items: list[int] = items
        self.expr = expr
        self._test = test
        self.inspect_count: int = 0

    def op(self, x) -> int:
        _, op, rhs = self.expr

        if rhs == 'old':
            return x * x
        else:
            if op == '+':
                return x + int(rhs)
            else:
                return x * int(rhs)

    def test(self, x) -> int:
        self.inspect_count += 1
        div, cond1, cond2 = self._test

        if (x % div == 0):
            return cond1, x / div
        else:
            return cond2, x 

def parse_numbers(line: str) -> list[int]:
    return list(map(int, re.findall(r'\d+', line)))

def parse_op(line: str):
    _, expr = line.split("Operation: new =")
    return expr.strip().split()


def parse_monkeys(data: list[str]) -> list[Monkey]:
    monkeys = []

    for i in range(0, len(data), 7):
       items = parse_numbers(data[i+1])
       expr = parse_op(data[i+2])
       div = parse_numbers(data[i+3])[0]
       cond1 = parse_numbers(data[i+4])[0]
       cond2 = parse_numbers(data[i+5])[0]

       monkeys.append(Monkey(items, expr, (div, cond1, cond2)))

    return monkeys

def print_items(monkeys: list[Monkey]):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {m.items}')

def print_activity(monkeys: list[Monkey]):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: inspected items {m.inspect_count} times.')

def part_one(data: list[str]) -> int:
    return 0
    monkeys = parse_monkeys(data)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop(0)
                worry_level = int(monkey.op(item) / 3)
                throw_to, _ = monkey.test(worry_level)

                monkeys[throw_to].items.append(worry_level)

        #print(f'After round {i+1}, the monkeys are holding items with these worry levels:')
        #print_items(monkeys)

    print_activity(monkeys)

    activity_counts = sorted([m.inspect_count for m in monkeys], reverse=True)[:2]

    return activity_counts[0] * activity_counts[1]


def part_two(data: list[str]) -> int:
    monkeys = parse_monkeys(data)
    #activity_sum = [0 for _ in range(len(monkeys))]

    activity_changes_dict = {}

    for i in range(20):
        activities_before = [m.inspect_count for m in monkeys]

        for monkey in monkeys:
            for item in monkey.items:
                worry_level = monkey.op(item)
                throw_to, n = monkey.test(worry_level)

                monkeys[throw_to].items.append(n)

            monkey.items = []
        
        activity_changes = [m.inspect_count - activities_before[i] for i, m in enumerate(monkeys)]
        ac = str(activity_changes)


        # if ac in activity_changes_dict:
        #     activity_changes_dict[ac] += 1
        # else:
        #     activity_changes_dict[ac] = 1
        # activity_sum = [ac + activity_sum[i] for i, ac in enumerate(activity_changes)]
        # activity__average = [a / (i+1) for a in activity_sum]
        # print(i, activity_changes, activity_sum, activity__average)
        # if i % 20 == 0:
        #     print(i)
        #print(f'Turn {i}')
        #print_items(monkeys)

    # print('Calculated after 1000:')

    # for i, a in enumerate(activity_sum):
    #     total = int((a / 300) * 1000)
    #     print (f'Monkey {i+1}: inspected items {total} times.')

    print_activity(monkeys)

    # l = sorted(list(activity_changes_dict.items()), key=lambda t: t[1], reverse=True)

    # for k, v in l:
    #     print(f'{k}: {v}')

    activity_counts = sorted([m.inspect_count for m in monkeys], reverse=True)[:2]

    return activity_counts[0] * activity_counts[1]


def main():
    print('Day 11: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day11_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day11', '\n'))))
    print('Day 11: Answer for Part 2: {}'.format(
        part_two(read_input('../tests/inputs/test_input_day11_1.txt', '\n'))))
        #part_two(read_input('../inputs/input_day11', '\n'))))


if __name__ == "__main__":
    main()
