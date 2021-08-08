from src.common.util import read_input
from collections import deque
from tqdm import tqdm

def crab_cups(cups: deque, moves: int):
    for _ in tqdm(range(moves)):
        current = cups.popleft()
        cups.append(current)

        pick_up = []
        for _ in range(3):
            pick_up.append(cups.popleft())

        destination = max(cups) if current - 1 < min(cups) else current - 1
        while destination in pick_up:
            destination = max(cups) if destination - 1 < min(cups) else destination - 1

        destination = cups.index(destination)

        for p in pick_up[::-1]:
            cups.insert(destination + 1, p)

    return cups

def crab_cups_opt(cups, moves):
    i = 0
    for i in tqdm(range(moves)):
        i+=1
    return cups

def part_one(input, nr_moves=100):
    cups = [int(i) for i in input[0]]
    cups = deque(cups, maxlen=len(cups))

    cups = crab_cups(cups, int(nr_moves))
    cups.rotate(-cups.index(1))
    cups.remove(1)

    return sum([10 ** i * c for i, c in enumerate(list(cups)[::-1])])


def part_two(input, nr_moves=10e6):
    cups = [int(i) for i in input[0]]
    cups = deque(cups, maxlen=int(1e6))
    cups.extend(range(max(cups) + 1, int(1e6)))

    cups = crab_cups_opt(cups, int(nr_moves))
    test = cups.index(1)

    return 0


def main():
    print('Day 23: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day23.txt', '\n'))))
    print('Day 23: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day23.txt', '\n'))))


if __name__ == "__main__":
    main()
