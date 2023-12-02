# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day02 import part_one, part_two
from src.common.util import read_input


class Day02Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(
            part_one(read_input('tests/inputs/test_input_day02_1.txt', '\n')), 8)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(read_input('tests/inputs/test_input_day02_1.txt', '\n')), 2286)


if __name__ == '__main__':
    unittest.main()
