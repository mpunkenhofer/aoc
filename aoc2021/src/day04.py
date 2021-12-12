from common.util import read_input
from typing import List
import numpy as np

BINGO_GRIDSIZE = 5

class BingoBoard:
    def __init__(self, rows) -> None:
        self.numbers = np.array([list(map(int, row.split())) for row in rows])
        self._marked = np.zeros((BINGO_GRIDSIZE, BINGO_GRIDSIZE))

    def mark(self, number):
        m = np.where(self.numbers == number)
        self._marked[m] = 1
        return self.check()

    def check(self):
        cols = np.sum(self._marked, axis=0)
        rows = np.sum(self._marked, axis=1)
        return (cols == BINGO_GRIDSIZE).sum() > 0 or (rows == BINGO_GRIDSIZE).sum() > 0 

    def get(self):
        return self.numbers

    def unmarked_sum(self):
        return self.numbers[np.where(self._marked == 0)].sum()

def init_boards(data) -> List[BingoBoard]:
    i, boards = 0, []

    while i < len(data):
        if data[i] == '':
            i += 1
        else:
            boards.append(BingoBoard(data[i:i+BINGO_GRIDSIZE]))
            i += BINGO_GRIDSIZE
    
    return boards

def part_one(data):
    numbers = list(map(int, data[0].split(',')))
    boards = init_boards(data[1:])  

    for n in numbers:
        for b in boards:
            if b.mark(n):
                return b.unmarked_sum() * n
    return -1


def part_two(data):
    numbers = list(map(int, data[0].split(',')))
    boards = np.array(init_boards(data[1:]))

    latest_score = 0

    for n in numbers:
        if len(boards) < 1:
            break
        
        bingo_boards = []

        for i in range(len(boards)):
            b = boards[i]
            if b.mark(n):
                latest_score = b.unmarked_sum() * n
                bingo_boards.append(i)

        boards = np.delete(boards, bingo_boards)

    return latest_score


def main():
    print('Day 04: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day04.txt', '\n'))))
    print('Day 04: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day04.txt', '\n'))))


if __name__ == "__main__":
    main()
