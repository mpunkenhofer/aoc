# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day07 import part_one, part_two
from src.common.util import read_input


class Day07Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(
            part_one(read_input('tests/inputs/test_input_day07_1.txt', '\n')), 95437)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(read_input('tests/inputs/test_input_day07_1.txt', '\n')), 24933642)


if __name__ == '__main__':
    unittest.main()
