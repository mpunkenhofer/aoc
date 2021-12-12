from common.util import read_input
import numpy as np

def part_one(data):
    data = [list(map(int, d)) for d in data]
    data = np.array(data)
    ones = np.sum(data, axis=0)

    rows, cols = data.shape

    gamma = 0

    for i in range(len(ones)):
        if ones[i] > rows / 2:
            gamma |= (1 << (cols - (i + 1)))
    
    epsilon = ~gamma & (2 ** cols - 1)

    #print('g: {:12b}\ne: {:12b}'.format(gamma, epsilon))

    return epsilon * gamma

def bin_array_to_dec(a):
    number = 0
    nr_bits = len(a)

    for i in range(nr_bits):
        if a[i] == 1:
            number |= (1 << (nr_bits - (i + 1)))

    return number

def calculate_rating(data, communality):
    for i in range(data.shape[1]):
        ones = data[:, i].sum()
        zeros = len(data) - ones

        c = communality(ones, zeros)

        remove = []

        for row in range(len(data)):
            if data[row, i] != c:
                remove.append(row)

        data = np.delete(data, remove, 0)

        if len(data) == 1:
            return bin_array_to_dec(data[0])   

    raise RuntimeError('Failed to calculate a rating.')

def part_two(data):
    data = [list(map(int, d)) for d in data]
    data = np.array(data)
    
    o_rating = calculate_rating(data, lambda ones, zeros: 1 if ones > zeros or ones == zeros else 0)
    co2_rating = calculate_rating(data, lambda ones, zeros: 1 if ones < zeros and ones != zeros else 0)

    return o_rating * co2_rating


def main():
    print('Day 3: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day03.txt', '\n'))))
    print('Day 3: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day03.txt', '\n'))))


if __name__ == "__main__":
    main()
