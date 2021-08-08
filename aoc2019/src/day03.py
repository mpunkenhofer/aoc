from common.util import read_input


def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    return (px, py)


def ccw(p, q, r):
    return (r[1] - p[1]) * (q[0] - p[0]) > (q[1] - p[1]) * (r[0] - p[0])


def intersect(p1, p2, q1, q2):
    return ccw(p1, q1, q2) != ccw(p2, q1, q2) and ccw(p1, p2, q1) != ccw(p1, p2, q2)


def to_points(path):
    x, y = 0, 0

    coords = [(x, y)]

    for p in path:
        direction = p[0]
        steps = int(p[1:])

        if direction == 'U':
            y += steps
        elif direction == 'D':
            y -= steps
        elif direction == 'R':
            x += steps
        elif direction == 'L':
            x -= steps

        coords.append((x, y))

    return coords


def taxicab_distance(p1, p2, q1, q2):
    return abs(p1 - q1) + abs(p2 - q2)


def get_intersection_segments(wire1, wire2):
    intersections = []

    for i in range(len(wire1) - 1):
        for j in range(len(wire2) - 1):

            if intersect(wire1[i], wire1[i + 1], wire2[j], wire2[j + 1]):
                intersections.append((i, j))

    return intersections


def get_intersection_points(wire1, wire2):
    # get the wire segments which intersect
    intersections = get_intersection_segments(wire1, wire2)
    # calculate exact point of intersection
    intersection_points = [intersection(wire1[i][0], wire1[i][1], wire1[i + 1][0], wire1[i + 1][1],
                                        wire2[j][0], wire2[j][1], wire2[j + 1][0], wire2[j + 1][1])
                           for (i, j) in intersections]

    return intersection_points


def get_min_distance(wire1, wire2):
    distances = [taxicab_distance(0, 0, p[0], p[1]) for p in get_intersection_points(wire1, wire2)]

    return min(distances)


def get_length(wire, end):
    if end > len(wire) or end < 1:
        return -1

    total = 0

    for i in range(end):
        x1, y1 = wire[i]
        x2, y2 = wire[i + 1]

        if x1 != x2:
            total += abs(x2 - x1)
        elif y1 != y2:
            total += abs(y2 - y1)

    return total


def get_min_delay(wire1, wire2):
    intersections = zip(get_intersection_segments(wire1, wire2), get_intersection_points(wire1, wire2))

    lengths = []

    for inter in intersections:
        (w1_end, w2_end), (x, y) = inter
        w1_segment_len = get_length(wire1, w1_end)
        w2_segment_len = get_length(wire2, w2_end)
        w1_intersect_seg_x, w1_intersect_seg_y = wire1[w1_end]
        w2_intersect_seg_x, w2_intersect_seg_y = wire2[w2_end]
        w1_seg_to_intersect = taxicab_distance(w1_intersect_seg_x, w1_intersect_seg_y, x, y)
        w2_seg_to_intersect = taxicab_distance(w2_intersect_seg_x, w2_intersect_seg_y, x, y)

        lengths.append(w1_segment_len + w1_seg_to_intersect + w2_segment_len + w2_seg_to_intersect)

    return min(lengths)


def main():
    path1, path2 = read_input('input', separator='\n')
    wire1, wire2 = to_points(str.split(path1, ',')), to_points(str.split(path2, ','))

    min_dist = get_min_distance(wire1, wire2)
    print('Answer to Day 3 - Part 1: {}'.format(min_dist))

    min_delay = get_min_delay(wire1, wire2)
    print('Answer to Day 3 - Part 2: {}'.format(min_delay))


if __name__ == "__main__":
    main()
