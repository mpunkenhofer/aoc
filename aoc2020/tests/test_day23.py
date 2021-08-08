# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day23 import part_one, part_two
from src.common.util import read_input

class Day23Tests(unittest.TestCase):
    def test_part_one_10(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day23_1.txt', '\n'), 10), 92658374)

    def test_part_one_100(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day23_1.txt', '\n'), 100), 67384529)

    #def test_part_two(self):
        #self.assertEqual(part_two(read_input('tests/inputs/test_input_day23_1.txt', '\n'), 10e6), 149245887792)

if __name__ == '__main__':
    unittest.main()