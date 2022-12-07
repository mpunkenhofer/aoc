from src.common.util import read_input
import re


class File:
    def __init__(self, name, size=0) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f'- {self.name} (file, size={self.size})'


class Directory:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.size = 0
        self.parent = parent
        self.files: list[File] = []
        self.children: list[Directory] = []

    def __str__(self) -> str:
        return f'- {self.name} ' + ('(dir)' if self.size == 0 else f'(dir, size={self.size})')


def cd(current: Directory, target: str) -> Directory:
    if target == '..':
        if (current.parent != None):
            return current.parent
        else:
            print(
                f'.. failed. There exists no parent directory for: {current.name}.')
            return current
    elif target == '/':
        # Go to root manually
        c = current

        while c.parent != None:
            c = c.parent

        return c
    else:
        for child in current.children:
            if child.name == target:
                return child

        print(
            f'Directory: {target} not found in this directory: {current.name}.')
        return current


def mkdir(current: Directory, name: str) -> Directory:
    new_dir = Directory(name, current)
    current.children.append(new_dir)
    return new_dir


def print_dirs(current: Directory, depth=0):
    spaces = ' ' * 2 * depth
    print(spaces, current)

    for child in current.children:
        print_dirs(child, depth + 1)

    for file in current.files:
        print(spaces, '  ', file)


def create_dirs(data: list[str]) -> Directory:
    current = Directory('/')

    for line in data:
        tokens = line.split(' ')

        if (len(tokens) < 2):
            continue

        if tokens[0] == '$':
            if tokens[1] == 'cd':
                current = cd(current, tokens[2])
        else:
            if tokens[0] == 'dir':
                mkdir(current, tokens[1])
            else:
                size = int(tokens[0])
                name = tokens[1]
                current.files.append(File(name, size))

    root = cd(current, '/')

    return root


def calc_size(current: Directory) -> int:
    size = sum(map(lambda f: f.size, current.files))

    for child in current.children:
        size += calc_size(child)

    current.size = size

    return size


def filter_dirs(current: Directory, threshold=100000):
    def f(c: Directory, t: int, result: list[int]):
        if c.size < threshold:
            result.append(c.size)

        for child in c.children:
            f(child, t, result)

        return result

    return f(current, threshold, [])


def stats(current: Directory):
    total = 70000000
    return total - current.size, current.size, total


def part_one(data: list[str]) -> int:
    root = create_dirs(data)
    calc_size(root)
    # print_dirs(root)
    return sum(filter_dirs(root))


def part_two(data: list[str]) -> int:
    root = create_dirs(data)
    calc_size(root)

    update_size = 30000000
    available, used, total = stats(root)
    required = update_size - available
    print(
        f'Storage: available: {available}, used: {used}, total: {total} required: {required}.')

    candidates = sorted(filter_dirs(root, update_size))

    for c in candidates:
        if c > required:
            return c

    return -1


def main():
    print('Day 07: Answer for Part 1: {}'.format(
        # part_one(read_input('../tests/inputs/test_input_day07_1.txt', '\n'))))
        part_one(read_input('../inputs/input_day07', '\n'))))
    print('Day 07: Answer for Part 2: {}'.format(
        # part_two(read_input('../tests/inputs/test_input_day07_1.txt', '\n'))))
        part_two(read_input('../inputs/input_day07', '\n'))))


if __name__ == "__main__":
    main()
