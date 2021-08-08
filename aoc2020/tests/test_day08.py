# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day8 import part_one, part_two
from src.common.util import read_input

class Day8Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day08_1.txt', '\n')), 5)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day08_2.txt', '\n')), 8)

if __name__ == '__main__':
    unittest.main()