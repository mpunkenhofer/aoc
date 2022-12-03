# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day03 import part_one, part_two
from src.common.util import read_input


class Day03Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(
            part_one(read_input('tests/inputs/test_input_day03_1.txt', '\n')), 157)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(read_input('tests/inputs/test_input_day03_1.txt', '\n')), 70)


if __name__ == '__main__':
    unittest.main()
