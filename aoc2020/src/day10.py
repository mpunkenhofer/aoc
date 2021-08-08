from src.common.util import read_input


def get_differences(adapters):
    differences = {}

    for i in range(len(adapters) - 1):
        d = abs(adapters[i] - adapters[i + 1])
        differences[d] = differences[d] + 1 if d in differences else 1

    return differences


def part_one(input):
    adapters = [int(i) for i in input if i]

    adapter_chain = sorted(adapters)
    adapter_chain = [0] + adapter_chain + [adapter_chain[-1] + 3]

    diffs = get_differences(adapter_chain)

    return diffs[1] * diffs[3]


def part_two(input):
    adapters = [int(i) for i in input if i]

    adapter_chain = sorted(adapters)
    adapter_chain.append(adapter_chain[-1] + 3)

    cost = {0: 1}

    for a in adapter_chain:
        cost[a] = cost.get(a - 3, 0) + cost.get(a - 2, 0) + cost.get(a - 1, 0)

    return cost[adapter_chain[-1]]


def main():
    print('Day 10: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day10.txt', '\n'))))
    print('Day 10: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day10.txt', '\n'))))


if __name__ == "__main__":
    main()
