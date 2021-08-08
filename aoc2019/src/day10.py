from common.util import read_input
import math
import itertools
import numpy as np


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def is_between(p, n, q, epsilon=1e-6):
    return -epsilon < ((distance(p, n) + distance(n, q)) - distance(p, q)) < epsilon


def is_on(a, b, c):
    return collinear(a, b, c) and (within(a[0], c[0], b[0]) if a[0] != b[0] else within(a[1], c[1], b[1]))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def within(p, q, r):
    return p <= q <= r or r <= q <= p


def get_asteroid_coordinates(asteroid_map):
    asteroid_coordinates = []

    for i in range(len(asteroid_map)):
        for j in range(len(asteroid_map[i])):
            if asteroid_map[i][j] == '#':
                asteroid_coordinates.append((j, i))
    return asteroid_coordinates


def new_monitor_station(asteroid_map):
    if len(asteroid_map) < 4:
        return (0, 0), 0

    asteroid_coords = get_asteroid_coordinates(asteroid_map)

    asteroids_in_view = {}

    for i, asteroid in enumerate(asteroid_coords):
        neighbors = asteroid_coords[:i] + asteroid_coords[i + 1:]
        asteroids_in_view[asteroid] = neighbors.copy()

        for j, neighbor in enumerate(neighbors):
            others = neighbors[:j] + neighbors[j + 1:]
            for o in others:
                if is_on(asteroid, neighbor, o):
                    if neighbor in asteroids_in_view[asteroid]:
                        asteroids_in_view[asteroid].remove(neighbor)

    # triples = list(itertools.combinations(asteroid_coords, 3))
    #
    # asteroids_in_view = {a: set() for a in asteroid_coords}
    #
    # for triple in triples:
    #     start, mid, end = triple
    #
    #     if is_on(start, mid, end):
    #         asteroids_in_view[start].add(mid)
    #         asteroids_in_view[end].add(end)
    #
    #     if is_on(start, end, mid):
    #         asteroids_in_view[start].add(start)
    #         asteroids_in_view[mid].add(end)
    #
    #     if is_on(end, mid, start):
    #         asteroids_in_view[start].add(start)
    #         asteroids_in_view[end].add(end)

    coord, asteroid_count = (0, 0), 0

    for k, v in asteroids_in_view.items():
        if len(v) > asteroid_count:
            coord, asteroid_count = k, len(v)

    return coord, asteroid_count


def vaporize_asteroid(asteroid_map, monitor_station, nr=0):
    if len(asteroid_map) < 4:
        return (0, 0), 0

    width = len(asteroid_map[0])
    height = len(asteroid_map)

    diagonal = math.ceil(math.sqrt(width ** 2 + height ** 2))

    vaporized_asteroids = []
    last_len = -1

    while nr >= len(vaporized_asteroids) != last_len:
        last_len = len(vaporized_asteroids)

        for phi in range(360):
            direction = np.array([math.sin(math.radians(phi)), math.cos(math.radians(phi))])

            vaporized = monitor_station

            for r in range(1, diagonal + 1):
                pr = (r * direction) * [1, -1]
                current = (monitor_station + pr)

                if current[0] >= width or current[1] >= height or current[0] < 0 or current[1] < 0:
                    break

                if np.array_equal(monitor_station, current):
                    continue

                x, y = int(current[0]), int(current[1])

                if y < height and x < width and asteroid_map[y][x] == '#':
                    if vaporized == monitor_station:
                        vaporized = (x, y)
                        asteroid_map[y] = asteroid_map[y][:x] + '.' + asteroid_map[y][x+1:]
                    if not is_on(monitor_station, (x, y), vaporized):
                        break
                    else:
                        asteroid_map[y] = asteroid_map[y][:x] + 'x' + asteroid_map[y][x+1:]

            if vaporized != monitor_station:
                vaporized_asteroids += [vaporized]

        for i in range(len(asteroid_map)):
            for j in range(len(asteroid_map[i])):
                if asteroid_map[i][j] == 'x':
                    asteroid_map[i] = asteroid_map[i][:j] + '#' + asteroid_map[i][j+1:]

    if nr < len(vaporized_asteroids):
        return vaporized_asteroids[nr]
    else:
        return -1, -1


def main():
    asteroid_map = read_input('test_input4', '\n')
    print('Answer for Day10 - Part 1: {}'.format(new_monitor_station(asteroid_map)))
    print('Answer for Day10 - Part 2: {}'.format(vaporize_asteroid(asteroid_map, (11, 13), 200)))


if __name__ == "__main__":
    main()
