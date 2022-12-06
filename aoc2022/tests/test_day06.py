# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day06 import part_one, part_two
from src.common.util import read_input


class Day06Tests(unittest.TestCase):
    def test_part_one_0(self):
        self.assertEqual(
            part_one(['mjqjpqmgbljsphdztnvjfqwrcgsmlb']), 7)

    def test_part_one_1(self):
        self.assertEqual(
            part_one(['bvwbjplbgvbhsrlpgdmjqwftvncz']), 5)

    def test_part_one_2(self):
        self.assertEqual(
            part_one(['nppdvjthqldpwncqszvftbrmjlhg']), 6)

    def test_part_one_3(self):
        self.assertEqual(
            part_one(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']), 10)

    def test_part_one_4(self):
        self.assertEqual(
            part_one(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']), 11)

    def test_part_two_1(self):
        self.assertEqual(
            part_two(['mjqjpqmgbljsphdztnvjfqwrcgsmlb']), 19)

    def test_part_two_2(self):
        self.assertEqual(
            part_two(['bvwbjplbgvbhsrlpgdmjqwftvncz']), 23)

    def test_part_two_3(self):
        self.assertEqual(
            part_two(['nppdvjthqldpwncqszvftbrmjlhg']), 23)

    def test_part_two_4(self):
        self.assertEqual(
            part_two(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']), 29)

    def test_part_two_5(self):
        self.assertEqual(
            part_two(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']), 26)


if __name__ == '__main__':
    unittest.main()
