# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import os
from typing import List
import unittest
from src.day03 import part_one, part_two
from src.common.util import read_input


    
class Day03Tests(unittest.TestCase):
    def setUp(self):
        # Get the directory of the current script
        current_script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the input file based on the script's location
        self.input_file_path = os.path.join(current_script_dir, 'inputs')

    def load_data(self, input_file: str) -> List[str]:
        path = os.path.join(self.input_file_path, input_file) 
        return read_input(path, '\n')

    def test_part_one_1(self):
        self.assertEqual(
            part_one(self.load_data('test_input_day03_1.txt')), 4361)
    
    def test_part_one_2(self):
        self.assertEqual(
            part_one(self.load_data('test_input_day03_2.txt')), 2133)

    def test_part_one_3(self):
        self.assertEqual(
            part_one(self.load_data('test_input_day03_3.txt')), 10000 + 10 + 2 * 100)
        
    def test_part_two_1(self):
        self.assertEqual(
            part_two(self.load_data('test_input_day03_1.txt')), 467835)


if __name__ == '__main__':
    unittest.main()
