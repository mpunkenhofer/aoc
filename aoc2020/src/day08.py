from src.common.util import read_input
import re

def run_program(program):
    ip = 0
    accumulator = 0
    terminated = False

    while True:
        if ip >= len(program):
            terminated = True
            break

        instruction = program[ip]

        match = re.match(r'([^\s]+)\s((\+|-)\d+)(\s\*)?', instruction)

        program = program[:ip] + [program[ip] + ' *'] + program[ip+1:]

        if not match:
            break

        op, value, marked = match.group(1), int(match.group(2)), match.group(4) is not None

        if marked:
            break

        if op == 'acc':
            accumulator += value
            ip += 1
        elif op == 'nop':
            ip += 1
        elif op == 'jmp':
            ip += value

    return accumulator, terminated

def part_one(input):
    acc, _ = run_program(input)
    return acc


def part_two(input):
    lines = []

    for i, line in enumerate(input):
        if line.startswith('jmp'):
            lines.append((i, 'jmp'))
        elif line.startswith('nop'):
            lines.append((i, 'nop'))

    acc, terminated = 0, False

    for i, op in lines:
        if op == 'jmp':
            repaired_prog = input[:i] + [input[i].replace('jmp', 'nop')] + input[i+1:]
        elif op == 'nop':
            repaired_prog = input[:i] + [input[i].replace('nop', 'jmp')] + input[i+1:]

        acc, terminated = run_program(repaired_prog)

        if terminated:
            break

    print('Program terminated ? -> {}'.format(terminated))

    return acc


def main():
    print('Day 8: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day8.txt', '\n'))))
    print('Day 8: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day8.txt', '\n'))))


if __name__ == "__main__":
    main()
