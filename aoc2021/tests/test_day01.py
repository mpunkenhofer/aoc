# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day01 import part_one, part_two

class Day01Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([0]), 1)

    def test_part_two(self):
        self.assertEqual(part_two([0]), 1)

if __name__ == '__main__':
    unittest.main()