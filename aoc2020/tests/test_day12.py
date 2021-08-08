# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day12 import part_one, part_two


class Day12Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(['F10',
                                   'N3',
                                   'F7',
                                   'R90',
                                   'F11']), 25)

    def test_part_two(self):
        self.assertEqual(part_two(['F10',
                                   'N3',
                                   'F7',
                                   'R90',
                                   'F11']), 286)


if __name__ == '__main__':
    unittest.main()
