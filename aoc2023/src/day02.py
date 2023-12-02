from src.common.util import read_input
import numpy as np
import re

def parse_data(data: list[str]):
    games = []

    for line in data:
        _, rest = line.split(':')
        sets = rest.split(';')

        draws = []

        for s in sets:
            rgb = [0, 0, 0]

            for i, color in enumerate(['red', 'green', 'blue']):
                m = re.search(rf'(\d+) {color}', s)

                if m:
                    value = m.group(1)
                    rgb[i] = int(value)

            draws.append(rgb)

        games.append(draws)

    return games

def part_one(data: list[str], limit=np.array([12, 13, 14])) -> int:
    games = parse_data(data)
    id_sum = 0

    for i, game in enumerate(games):
        possible = 0

        for draw in game:
            if np.all(np.array(draw) <= limit):
                possible += 1
        
        if len(game) == possible:
            id_sum += i + 1

    return id_sum

def part_two(data: list[str]) -> int:
    games = parse_data(data)
    power_sum = 0

    for game in games:
        max_cubes = np.zeros((3,))

        for draw in game:
            max_cubes = np.maximum(max_cubes, np.array(draw))
        
        power_sum += np.prod(max_cubes)

    return int(power_sum)


def main():
    print('Day 02: Answer for Part 1: {}'.format(
        part_one(read_input('../inputs/input_day02', '\n'))))
    print('Day 02: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day02', '\n'))))


if __name__ == "__main__":
    main()
