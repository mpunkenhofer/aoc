import unittest

from common.util import read_input
from .day6 import (calculate_orbits, calculate_min_transfers)


class MyTestCase(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(calculate_orbits(read_input('day6/test_input1', '\n')), 42)

    def test_tc2(self):
        self.assertEqual(calculate_min_transfers(read_input('day6/test_input2', '\n'), 'YOU', 'SAN'), 4)


if __name__ == '__main__':
    unittest.main()
