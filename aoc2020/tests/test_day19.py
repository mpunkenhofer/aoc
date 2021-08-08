# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day19 import part_one, part_two
from src.common.util import read_input

class Day19Tests(unittest.TestCase):
    def test_part_one_1(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day19_1.txt', '\n')), 2)

    def test_part_one_2(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day19_2.txt', '\n')), 0)

    def test_part_two(self):
        self.assertEqual(part_two(''), 0)

if __name__ == '__main__':
    unittest.main()