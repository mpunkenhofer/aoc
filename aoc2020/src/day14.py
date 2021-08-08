import re
from src.common.util import read_input
from itertools import product

def run_program(input, driver):
    current_mask = 'X' * 36
    mem = {}

    for line in input:
        mask_match = re.match(r'mask = ([X01]+)', line)
        mem_match = re.match(r'mem\[(\d+)\] = (\d+)', line)

        if mask_match:
            current_mask = mask_match.group(1)
        if mem_match:
            addr, value = int(mem_match.group(1)), int(mem_match.group(2))
            mem.update(driver(current_mask, addr, value))

    return sum(mem.values())

def apply_mask(mask, addr, value):
    value = '{:036b}'.format(value)
    result = '0b'

    for (mi, vi) in zip(mask, value):
        if mi != 'X':
            result += mi
        else:
            result += vi

    return {addr: int(result, 2)}

def replace_floating(mask, positions, replacements):
    if len(positions) != len(replacements):
        raise RuntimeError('count of positions != replacements')

    for i, p in enumerate(positions):
        mask = mask[:p] + replacements[i] + mask[p+1:]
    
    return mask

def addr_decoder(mask, addr, value):
    addr = '{:036b}'.format(addr)
    result = ''

    for (mi, ai) in zip(mask, addr):
        if mi == '1' or mi == 'X':
            result += mi
        else:
            result += ai

    floating = result.count('X')
    mem = {}

    for f in product('10', repeat=floating):
        addr = replace_floating(result, [i for i, ltr in enumerate(result) if ltr == 'X'], f)
        mem[int('0b' + addr, 2)] = value

    return mem

def part_one(input):
    return run_program(input, apply_mask)

def part_two(input):
    return run_program(input, addr_decoder)


def main():
    print('Day 14: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day14.txt', '\n'))))
    print('Day 14: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day14.txt', '\n'))))


if __name__ == "__main__":
    main()
