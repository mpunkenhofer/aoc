# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day24 import part_one, part_two
from src.common.util import read_input

class Day24Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day24_1.txt', '\n')), 10)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day24_1.txt', '\n')), 2208)

if __name__ == '__main__':
    unittest.main()