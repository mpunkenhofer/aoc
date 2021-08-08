import re
import numpy as np
from src.common.util import read_input


def parse_input(input):
    paths = []

    for line in input:
        paths.append(re.findall(r'e|se|sw|w|nw|ne', line))

    return paths

def get_tiles(path, start=[0, 0]):
    tiles = []

    current_tile = np.array(start)

    for direction in path:
        if direction == 'e':
            current_tile += [2, 0]
        elif direction == 'se':
            current_tile += [1, 1]
        elif direction == 'sw':
            current_tile += [-1, 1]
        elif direction == 'w':
            current_tile += [-2, 0]
        elif direction == 'nw':
            current_tile += [-1, -1]
        elif direction == 'ne':
            current_tile += [1, -1]
        else:
            raise RuntimeError('Unexpected Direction: {}'.format(direction))

        tiles.append(tuple(current_tile))

    return tiles

def flip_tiles(paths):
    filpped_tiles = {}

    for path in paths:
        final_tile = get_tiles(path)[-1]
        filpped_tiles[final_tile] = filpped_tiles.get(final_tile, 0) + 1

    return filpped_tiles

def hex_grind_neighbors(tile):
    return [tuple(np.array(tile) + n) for n in [[2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1], [1, -1]]]

def tile_exhibit(tiles: dict, day: int):
    for d in range(day):
        print(f'Day {d + 1}: {sum(tiles.values())}')
        tiles_snapshot = dict(tiles)

        for tile, is_black in tiles_snapshot.items():
            black_neighbors = 0
            neighbors = hex_grind_neighbors(tile)
            for neighbor in neighbors:
                if neighbor in tiles_snapshot:
                    black_neighbors += 1 if tiles_snapshot[neighbor] else 0
                else:
                    tiles[neighbor] = False

            if not is_black and black_neighbors == 2:
                tiles[tile] = True

            if is_black and (black_neighbors == 0 or black_neighbors > 2):
                tiles[tile] = False
        


    return tiles

def part_one(input):
    paths = parse_input(input)

    tiles = flip_tiles(paths)

    return len([v for v in tiles.values() if v % 2 != 0])


def part_two(input):
    paths = parse_input(input)

    tiles = flip_tiles(paths)

    for tile in tiles:
        tiles[tile] = True

    tiles = tile_exhibit(tiles, 100)

    return sum(tiles.values())


def main():
    print('Day 24: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day24.txt', '\n'))))
    print('Day 24: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day24.txt', '\n'))))


if __name__ == "__main__":
    main()
