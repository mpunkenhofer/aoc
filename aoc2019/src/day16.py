from common.util import read_input
import numpy as np


def fft(signal, phase, debug=False):
    pattern = [0, 1, 0, -1]
    debug_resolution = 8

    if debug:
        print('Input Signal: {}'.format(signal[:debug_resolution]))

    # matrix = np.tile(signal, (len(signal), 1))
    # signal = np.array(signal)
    # pattern = np.zeros((len(signal), 1))

    for i in range(1, phase + 1):
        for j in range(1, len(signal) + 1):
            total = 0
            k = j
            while k < len(signal) + 1:
                m = k
                while k < m + j and k < len(signal) + 1:
                    total += signal[k - 1] * pattern[int(k / j) % 4]
                    k += 1
                k += j

            digit = int(str(total)[-1])
            signal[j - 1] = digit

        if debug:
            print('After {:2d} {}: {}'.format(i, 'phases' if i > 1 else 'phase ', signal[:debug_resolution]))
            print(np.cumsum(np.array(signal)[::-1]))

    return signal


def main():
    output_resolution = 8
    input_signal = list(map(int, read_input('input')))
    signal = fft(input_signal, 21, True)
    print('Answer for Day16 - Part 1: {}'.format(''.join(map(str, signal[:output_resolution]))))

    input_signal *= 10000
    offset = int(''.join(map(str, input_signal[:7])))
    signal = fft(input_signal[offset:], 100, True)
    print('Answer for Day16 - Part 2: {}'.format(''.join(map(str, signal[:output_resolution]))))


if __name__ == "__main__":
    main()
