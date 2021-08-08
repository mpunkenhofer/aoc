# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day2 import part_one, part_two


class Day2Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(['1-3 a: abcde',
                                   '1-3 b: cdefg',
                                   '2-9 c: ccccccccc']), 2)

    def test_part_two(self):
        self.assertEqual(part_two(['1-3 a: abcde',
                                   '1-3 b: cdefg',
                                   '2-9 c: ccccccccc']), 2)


if __name__ == '__main__':
    unittest.main()
