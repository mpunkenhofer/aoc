import unittest

from common.util import read_input
from .day10 import new_monitor_station


class MyTestCase(unittest.TestCase):
    def test_tc0(self):
        asteroid_map = read_input('day10/test_input0', '\n')
        self.assertEqual(new_monitor_station(asteroid_map), ((3, 4), 8))

    def test_tc1(self):
        asteroid_map = read_input('day10/test_input1', '\n')
        self.assertEqual(new_monitor_station(asteroid_map), ((5, 8), 33))

    def test_tc2(self):
        asteroid_map = read_input('day10/test_input2', '\n')
        self.assertEqual(new_monitor_station(asteroid_map), ((1, 2), 35))

    def test_tc3(self):
        asteroid_map = read_input('day10/test_input3', '\n')
        self.assertEqual(new_monitor_station(asteroid_map), ((6, 3), 41))

    def test_tc4(self):
        asteroid_map = read_input('day10/test_input4', '\n')
        self.assertEqual(new_monitor_station(asteroid_map), ((11, 13), 210))


if __name__ == '__main__':
    unittest.main()
