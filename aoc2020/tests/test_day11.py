# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
from src.day11 import part_one, part_two, occupied_visible
from src.common.util import read_input


class Day11Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(read_input('tests/inputs/test_input_day11_1.txt', '\n'), 40, 20), 37)

    def test_occupied_visible_1(self):
        self.assertEqual(occupied_visible(['.......#.',
                                           '...#.....',
                                           '.#.......',
                                           '.........',
                                           '..#L....#',
                                           '....#....',
                                           '.........',
                                           '#........',
                                           '...#.....'], (3, 4)), 8)

    def test_occupied_visible_2(self):
        self.assertEqual(occupied_visible(['.............',
                                           '.L.L.#.#.#.#.',
                                           '.............'], (1, 1)), 0)

    def test_occupied_visible_3(self):
        self.assertEqual(occupied_visible(['.##.##.',
                                           '#.#.#.#',
                                           '##...##',
                                           '...L...',
                                           '##...##',
                                           '#.#.#.#',
                                           '.##.##.'], (0, 1)), 4)

    def test_occupied_visible_4(self):
        self.assertEqual(occupied_visible(['.##.##.',
                                           '#.#.#.#',
                                           '##...##',
                                           '...L...',
                                           '##...##',
                                           '#.#.#.#',
                                           '.##.##.'], (3, 3)), 0)

    def test_part_two(self):
        self.assertEqual(part_two(read_input('tests/inputs/test_input_day11_1.txt', '\n'), 40, 20), 26)


if __name__ == '__main__':
    unittest.main()
