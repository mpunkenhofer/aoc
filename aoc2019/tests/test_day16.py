import unittest
from common.util import read_input
from .day16 import fft


class MyTestCase(unittest.TestCase):
    def test_tc0(self):
        input_signal = list(map(int, read_input('day16/test_input0')))
        signal = fft(input_signal, 4)
        self.assertEqual(''.join(map(str, signal[:8])), '01029498')

    def test_tc1(self):
        input_signal = list(map(int, read_input('day16/test_input1')))
        signal = fft(input_signal, 100)
        self.assertEqual(''.join(map(str, signal[:8])), '24176176')

    def test_tc2(self):
        input_signal = list(map(int, read_input('day16/test_input2')))
        signal = fft(input_signal, 100)
        self.assertEqual(''.join(map(str, signal[:8])), '73745418')

    def test_tc3(self):
        input_signal = list(map(int, read_input('day16/test_input3')))
        signal = fft(input_signal, 100)
        self.assertEqual(''.join(map(str, signal[:8])), '52432133')

    # def test_tc4(self):
    #     input_signal = list(map(int, read_input('day16/test_input4')))
    #     signal = fft(input_signal, self.pattern, 4)
    #     self.assertEqual(''.join(map(str, signal[:8])), '84462026')


if __name__ == '__main__':
    unittest.main()
