import unittest

import common.util
from .day3 import (get_min_distance, to_points)


class MyTestCase(unittest.TestCase):
    def test_tc1(self):
        path1, path2 = common.util.read_input('day3/test_input1', separator='\n')
        wire1, wire2 = to_points(str.split(path1, ',')), to_points(str.split(path2, ','))
        min_dist = get_min_distance(wire1, wire2)
        self.assertAlmostEqual(min_dist, 159)

    def test_tc2(self):
        path1, path2 = common.util.read_input('day3/test_input2', separator='\n')
        wire1, wire2 = to_points(str.split(path1, ',')), to_points(str.split(path2, ','))
        min_dist = get_min_distance(wire1, wire2)
        self.assertAlmostEqual(min_dist, 135)


if __name__ == '__main__':
    unittest.main()
