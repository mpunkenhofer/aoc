# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day25 import part_one, part_two
from src.common.util import read_input

class Day25Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(['5764801', '17807724']), 14897079)

    def test_part_two(self):
        self.assertEqual(part_two(''), 0)

if __name__ == '__main__':
    unittest.main()