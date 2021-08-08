# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day5 import part_one, part_two

class Day5Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(['FBFBBFFRLR']), 357)
        self.assertEqual(part_one(['BFFFBBFRRR']), 567)
        self.assertEqual(part_one(['FFFBBBFRRR']), 119)
        self.assertEqual(part_one(['BBFFBBFRLL']), 820)

    def test_part_two(self):
        self.assertEqual(part_two([]), 0)

if __name__ == '__main__':
    unittest.main()