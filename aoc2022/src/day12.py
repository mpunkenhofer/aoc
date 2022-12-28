from src.common.util import read_input

class Node:
    def __init__(self, height, pos) -> None:
        self.height: int = height
        self.pos: tuple[int, int] = pos
        self.neighbors: list[Node] = []
        self.visited = False
        self.parent = None

def length(node: Node):
    i = 0

    while node is not None:
        node = node.parent
        i += 1
    
    return i

def to_list(node: Node):
    l = []

    while node is not None:
        l.append(node.pos)
        node = node.parent

    return l

def find_path(root: Node, goal, heuristic = lambda a, b: (b.height - a.height) <= 1):
    q: list[Node] = [root]
    root.visited = True

    while len(q) > 0:
        current = q.pop(0)
        neighbors = current.neighbors

        if goal(current):
            return current

        for n in neighbors:
            if not n.visited and heuristic(current, n):
                q.append(n)
                n.parent = current
                n.visited = True

        if len(q) == 0:
            print('alert!')
            print(to_list(current))

    return None

def print_path(path, width, height):
    map = [['.' for _ in range(width)] for _ in range(height)]

    for i in range(len(path)):
        current = path[i]
        next = path[i + 1] if i < len(path) - 1 else None

        x, y = current

        if next == None:
            map[y][x] = 'E'
        else:
            nx, ny = next
            dx, dy = x - nx, y - ny

            if dy == 1:
                map[y][x] = '^'
            elif dx == 1:
                map[y][x] = '<'
            elif dy == -1:
                map[y][x] = 'v'
            else:
                map[y][x] = '>'

    for line in map:
        print(''.join(line))

def parse_map(data: list[str]):
    start = end = None
    nodes = []

    y = 0
    for line in data:
        l = []
        x = 0
        for c in line:
            p = (x, y)
            if c == 'S':
                start = Node(1, p)
                l.append(start)
            elif c == 'E':
                end = Node(26, p)
                l.append(end)
            else:
                l.append(Node(ord(c) - 96, p))
            x += 1
        y += 1
        nodes.append(l)

    return nodes, start, end

def build_graph(map: list[list[Node]]):
    for y in range(len(map)):
        width = len(map[y])
        for x in range(width):
            for n in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + n[0], y + n[1]

                if (nx < 0 or ny < 0 or ny >= len(map) or nx >= len(map[y])):
                    continue

                map[y][x].neighbors.append(map[ny][nx])
    return 

def part_one(data: list[str]) -> int:
    map, start, end = parse_map(data)

    build_graph(map)

    p = find_path(start, lambda n: n.pos == end.pos)
    
    #print_path(to_list(p), len(map[0]), len(map))

    return length(p) - 1


def part_two(data: list[str]) -> int:
    map, _, end = parse_map(data)

    build_graph(map)

    p = find_path(end, lambda n: n.height == 1, lambda a, b: (a.height - b.height) <= 1)

    #print_path(to_list(p), len(map[0]), len(map))

    return length(p) - 1


def main():
    print('Day 12: Answer for Part 1: {}'.format(
        #part_one(read_input('../tests/inputs/test_input_day12_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day12', '\n'))))
    print('Day 12: Answer for Part 2: {}'.format(
        part_two(read_input('../inputs/input_day12', '\n'))))


if __name__ == "__main__":
    main()
