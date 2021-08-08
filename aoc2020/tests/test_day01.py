# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day1 import part_one, part_two

class Day1Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([1721, 979, 366, 299, 675, 1456]), 514579)

    def test_part_two(self):
        self.assertEqual(part_two([1721, 979, 366, 299, 675, 1456]), 241861950)

if __name__ == '__main__':
    unittest.main()