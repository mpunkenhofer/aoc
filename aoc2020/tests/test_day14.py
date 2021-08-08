# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day14 import part_one, part_two
from src.common.util import read_input

class Day14Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day14_1.txt', '\n')), 165)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day14_2.txt', '\n')), 208)

if __name__ == '__main__':
    unittest.main()