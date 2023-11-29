# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:00:04 2023

@author: User
"""

import unittest 
from even_num_sorter import even_number_sorter
num_list = [1,2,3,4,5,6,7,8,9,10]
num2 = [2, 4, 6, 8, 10]


class NumTest(unittest.TestCase):
    def test_num(self):
        sorted_numbers = even_number_sorter(num_list)
        self.assertSequenceEqual(sorted_numbers, num2)
unittest.main()