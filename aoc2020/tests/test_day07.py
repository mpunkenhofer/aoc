# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day7 import part_one, part_two
from src.common.util import read_input

class Day7Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day07_1.txt', '\n')), 4)

    def test_part_two_1(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day07_1.txt', '\n')), 32)

    def test_part_two_2(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day07_2.txt', '\n')), 126)

if __name__ == '__main__':
    unittest.main()