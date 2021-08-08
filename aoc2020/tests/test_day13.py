# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day13 import part_one, part_two


class Day13Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(['939',
                                   '7,13,x,x,59,x,31,19']), 295)

    def test_part_two_1(self):
        self.assertEqual(part_two(['939',
                                   '7,13,x,x,59,x,31,19']), 1068781)

    def test_part_two_2(self):
        self.assertEqual(part_two(['939',
                                   '17,x,13,19']), 3417)
                                
    def test_part_two_3(self):
        self.assertEqual(part_two(['939',
                                   '67,7,59,61']), 754018)

    def test_part_two_4(self):
        self.assertEqual(part_two(['939',
                                   '67,x,7,59,61']), 779210)

    def test_part_two_5(self):
        self.assertEqual(part_two(['939',
                                   '67,7,x,59,61']), 1261476)

    def test_part_two_6(self):
        self.assertEqual(part_two(['939',
                                   '1789,37,47,1889']), 1202161486)

if __name__ == '__main__':
    unittest.main()
