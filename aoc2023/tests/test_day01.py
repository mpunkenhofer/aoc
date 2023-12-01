# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day01 import part_one, part_two
from src.common.util import read_input


class Day01Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(
            part_one(read_input('inputs/test_input_day01_1.txt', '\n')), 142)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(read_input('inputs/test_input_day01_2.txt', '\n')), 281)


if __name__ == '__main__':
    unittest.main()
