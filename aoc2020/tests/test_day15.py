# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day15 import part_one, part_two
from src.common.util import read_input

class Day15Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one('0,3,6'.split(',')), 436)
        self.assertEqual(part_one('1,3,2'.split(',')), 1)
        self.assertEqual(part_one('2,1,3'.split(',')), 10)
        self.assertEqual(part_one('1,2,3'.split(',')), 27)
        self.assertEqual(part_one('2,3,1'.split(',')), 78)
        self.assertEqual(part_one('3,2,1'.split(',')), 438)
        self.assertEqual(part_one('3,1,2'.split(',')), 1836)

    def test_part_two(self):
        self.assertEqual(part_one('0,3,6'.split(',')), 175594)

if __name__ == '__main__':
    unittest.main()