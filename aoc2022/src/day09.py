from src.common.util import read_input

def distance(a, b):
    return abs(b - a)

def chebyshev_distance(a, b):
    return max(distance(a[0], b[0]), distance(a[1], b[1]))

def get_visited(path, part = 0):
    visited = {}

    for p in path[part]:
        loc = p
        if loc in visited:
            visited[loc] += 1
        else:
            visited[loc] = 1
    
    return visited

def simulate(moves, tail_length=1):
    path = [[(0, 0)] for _ in range(tail_length)]
    hx, hy = 0, 0

    for line in moves:
        l = line.split()
        dir, steps = l[0], int(l[1])

        i = 0

        while i < steps:
            if dir == 'U':
                hy += 1
            elif dir == 'D':
                hy -= 1
            elif dir == 'R':
                hx += 1
            elif dir == 'L':
                hx -= 1

            for j in range(tail_length):

                tx, ty = path[j][-1]

                if chebyshev_distance((hx, hy), (tx, ty)) > 1:
                    xd = hx - tx
                    yd = hy - ty

                    if xd != 0:
                        tx += 1 if xd > 0 else -1
                    if yd != 0:
                        ty += 1 if yd > 0 else -1

                    path[j].append((tx, ty))

            i += 1
    
    return path

def part_one(data: list[str]) -> int:    
    path = simulate(data)
    return len(get_visited(path).keys())


def part_two(data: list[str]) -> int:
    path = simulate(data, 9)
    return len(get_visited(path).keys())


def main():
    print('Day 09: Answer for Part 1: {}'.format(
        part_one(read_input('../tests/inputs/test_input_day09_1.txt', '\n'))))
        #part_one(read_input('../inputs/input_day09', '\n'))))
    print('Day 09: Answer for Part 2: {}'.format(
        part_two(read_input('../tests/inputs/test_input_day09_2.txt', '\n'))))
        # part_two(read_input('../inputs/input_day09', '\n'))))


if __name__ == "__main__":
    main()
