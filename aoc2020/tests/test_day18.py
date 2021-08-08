# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day18 import part_one, part_two
from src.common.util import read_input


class Day18Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([
            '2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']), 26 + 437 + 12240 + 13632)

    def test_part_two(self):
        self.assertEqual(part_two('1+1'), 2)


if __name__ == '__main__':
    unittest.main()
