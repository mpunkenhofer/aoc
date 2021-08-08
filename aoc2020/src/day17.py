from src.common.util import read_input
from functools import lru_cache
from itertools import product
import operator

def parse_input(input):
    cubes = []
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == '#':
                cubes.append((x, y, 0, 0))
    return cubes

@lru_cache(maxsize=64)
def get_neighbors(point, dimensions=3):
    neighbors = []

    for n in product([-1, 0, 1], repeat=min(len(point), dimensions)):
        p = tuple(map(operator.add, point, n))
        p += ((0,) * (max(0, len(point) - len(n))))  # pad zeros 

        if p != point:
            neighbors.append(p)

    return neighbors

def count_actives(cubes, coord, dimensions=3):
    actives = 0

    for n in get_neighbors(coord, dimensions):
        if n in cubes:
            actives += 1

    return actives

def perform_cycle(cubes, cycles=1, dimensions=3):
    for _ in range(cycles):
        active_cubes = []
        inactive_cubes = set()

        for cube in cubes:
            neighbors = get_neighbors(cube, dimensions)
            for n in neighbors:
                if n not in cubes:
                    inactive_cubes.add(n)
        
        """
        If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
        Otherwise, the cube becomes inactive.
        """

        for cube in cubes:
            active_neighbors = count_actives(cubes, cube, dimensions)
            if active_neighbors in (2, 3):
                active_cubes.append(cube)
        
        """
        If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
        Otherwise, the cube remains inactive.
        """

        for cube in inactive_cubes:
            active_neighbors = count_actives(cubes, cube, dimensions)
            if active_neighbors == 3:
                active_cubes.append(cube)
        
        cubes = active_cubes

    return active_cubes

def get_ascii_slices(cubes, z=[0]):
    min_x, max_x = min(cubes, key=lambda xyz: xyz[0])[0], max(cubes, key=lambda xyz: xyz[0])[0]
    min_y, max_y = min(cubes, key=lambda xyz: xyz[1])[1], max(cubes, key=lambda xyz: xyz[1])[1]

    slices = []

    for zi in z:
        lines = ['z={}'.format(zi)]
        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                if (x, y, zi) in cubes:
                    line += '#'
                else:
                    line += '.'
            lines.append(line)
        slices.append(lines)
    
    return slices

def print_slice(slices):
    for slice in slices:
        for line in slice:
            print(line)
        print('')

def print_example():
    input = read_input('tests/inputs/test_input_day17_1.txt', '\n')
    cubes = parse_input(input) 
    print_slice(get_ascii_slices(cubes))
    cubes = perform_cycle(cubes)
    print('After 1 cycle:')
    print_slice(get_ascii_slices(cubes, z=[-1, 0, 1]))
    cubes = perform_cycle(cubes)
    print('After 2 cycles:')
    print_slice(get_ascii_slices(cubes, z=[-2, -1, 0, 1, 2]))
    cubes = perform_cycle(cubes)
    print('After 3 cycles:')
    print_slice(get_ascii_slices(cubes, z=[-3, -2, -1, 0, 1, 2, 3]))

def part_one(input, cycles=6):
    return len(perform_cycle(parse_input(input), cycles=cycles))

def part_two(input, cycles=6, dimensions=4):
    return len(perform_cycle(parse_input(input), dimensions=dimensions, cycles=cycles))

def main():
    print('Day 17: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day17.txt', '\n'))))
    print('Day 17: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day17.txt', '\n'))))


if __name__ == "__main__":
    main()
