# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day6 import part_one, part_two


class Day6Tests(unittest.TestCase):
    test_input = """abc

a
b
c

ab
ac

a
a
a
a

b

"""

    def test_part_one(self):
        self.assertEqual(part_one(self.test_input.split('\n')), 11)

    def test_part_two(self):
        self.assertEqual(part_two(self.test_input.split('\n')), 6)


if __name__ == '__main__':
    unittest.main()
