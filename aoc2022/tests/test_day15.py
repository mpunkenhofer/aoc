# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day15 import part_one, part_two
from src.common.util import read_input


class Day15Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(
            part_one(read_input('tests/inputs/test_input_day15_1.txt', '\n'), 10), 26)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(read_input('tests/inputs/test_input_day15_1.txt', '\n'), 20), 56000011)


if __name__ == '__main__':
    unittest.main()
