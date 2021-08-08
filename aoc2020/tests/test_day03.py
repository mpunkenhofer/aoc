# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day3 import part_one, part_two


class Day3Tests(unittest.TestCase):
    test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
    """

    def test_part_one(self):
        self.assertEqual(part_one(self.test_input.split('\n')), 7)

    def test_part_two(self):
        self.assertEqual(part_two(self.test_input.split('\n')), 336)


if __name__ == '__main__':
    unittest.main()
