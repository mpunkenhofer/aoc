# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day17 import part_one, part_two
from src.common.util import read_input

class Day17Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day17_1.txt', '\n')), 112)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day17_1.txt', '\n')), 848)

if __name__ == '__main__':
    unittest.main()