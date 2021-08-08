# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day10 import part_one, part_two
from src.common.util import read_input

class Day10Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day10_1.txt', '\n')), 35)
    def test_part_one_2(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day10_2.txt', '\n')), 220)

    def test_part_two_1(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day10_1.txt', '\n')), 8)
    
    def test_part_two_2(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day10_2.txt', '\n')), 19208)

if __name__ == '__main__':
    unittest.main()