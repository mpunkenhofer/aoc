# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day22 import part_one, part_two
from src.common.util import read_input

class Day22Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day22_1.txt', '\n')), 306)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day22_1.txt', '\n')), 291)

    def test_infinite(self):
        self.assertGreater(part_two(read_input('tests/inputs/test_input_day22_2.txt', '\n')), 0)

if __name__ == '__main__':
    unittest.main()