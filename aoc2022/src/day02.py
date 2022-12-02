from src.common.util import read_input

RPS1 = {
    'AX': 4,    # Rock vs Rock          -> 1 + 3
    'AY': 8,    # Rock vs Paper         -> 2 + 6
    'AZ': 3,    # Rock vs Scissors      -> 3 + 0
    'BX': 1,    # Paper vs Rock         -> 1 + 0
    'BY': 5,    # Paper vs Paper        -> 2 + 3
    'BZ': 9,    # Paper vs Scissors     -> 3 + 6
    'CX': 7,    # Scissors vs Rock      -> 1 + 6
    'CY': 2,    # Scissors vs Paper     -> 2 + 0
    'CZ': 6,    # Scissors vs Scissors  -> 3 + 3
}

RPS2 = {
    'AX': 3,    # Rock vs Lose          -> 0 + 3
    'AY': 4,    # Rock vs Draw          -> 3 + 1
    'AZ': 8,    # Rock vs Win           -> 6 + 2
    'BX': 1,    # Paper vs Lose         -> 0 + 1
    'BY': 5,    # Paper vs Draw         -> 3 + 2
    'BZ': 9,    # Paper vs Win          -> 6 + 3
    'CX': 2,    # Scissors vs Lose      -> 0 + 2
    'CY': 6,    # Scissors vs Draw      -> 3 + 3
    'CZ': 7,    # Scissors vs Win       -> 6 + 1
}


def part_one(data: list[str]) -> int:
    score: int = 0

    for d in data:
        round = d.replace(" ", "")
        score += RPS1[round]

    return score


def part_two(data: list[str]) -> int:
    score: int = 0

    for d in data:
        round = d.replace(" ", "")
        score += RPS2[round]

    return score


def main():
    print('Day 02: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day02', '\n'))))
    print('Day 02: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day02', '\n'))))


if __name__ == "__main__":
    main()
