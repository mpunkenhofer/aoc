import numpy as np
from src.common.util import read_input


def manhatten_distance(position):
    return np.sum(np.abs(position))


def rotation_matrix(angle, clockwise=True):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    return np.array(((c, -s), (s, c))) if clockwise else np.array(((c, s), (-s, c)))


def part_one(input):
    epsilon = 1e-5
    position = np.array([[0.], [0.]])
    direction = np.array([[1.], [0.]])
    coords = [(0., 0.)]

    for p in input:
        action, value = p[0], int(p[1:])
        if action == 'F':
            position += value * direction
        elif action == 'N':
            position += np.array([[0], [-value]])
        elif action == 'S':
            position += np.array([[0], [value]])
        elif action == 'E':
            position += np.array([[value], [0]])
        elif action == 'W':
            position += np.array([[-value], [0]])
        elif action == 'L':
            r = rotation_matrix(value, False)
            direction = np.matmul(r, direction)
            direction[np.abs(direction) < epsilon] = 0
            continue
        elif action == 'R':
            r = rotation_matrix(value, True)
            direction = np.matmul(r, direction)
            direction[np.abs(direction) < epsilon] = 0
            continue

        coord = (position[0][0], position[1][0])
        coords.append(coord)

    return manhatten_distance(coords[-1])


def part_two(input):
    epsilon = 1e-5
    position = np.array([[0.], [0.]])
    waypoint = np.array([[10], [-1]])
    coords = [(0., 0.)]

    for p in input:
        action, value = p[0], int(p[1:])
        if action == 'F':
            position += value * waypoint
            coord = (position[0][0], position[1][0])
            coords.append(coord)
        elif action == 'N':
            waypoint += np.array([[0], [-value]])
        elif action == 'S':
            waypoint += np.array([[0], [value]])
        elif action == 'E':
            waypoint += np.array([[value], [0]])
        elif action == 'W':
            waypoint += np.array([[-value], [0]])
        elif action == 'L':
            r = rotation_matrix(value, False)
            waypoint = np.matmul(r, waypoint)
            waypoint[np.abs(waypoint) < epsilon] = 0
        elif action == 'R':
            r = rotation_matrix(value, True)
            waypoint = np.matmul(r, waypoint)
            waypoint[np.abs(waypoint) < epsilon] = 0

    return manhatten_distance(np.round(coords[-1]))


def main():
    print('Day 12: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day12.txt', '\n'))))
    print('Day 12: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day12.txt', '\n'))))


if __name__ == "__main__":
    main()
