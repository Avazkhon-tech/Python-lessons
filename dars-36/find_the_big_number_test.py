# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:58:10 2023

@author: User
"""

import unittest
from find_the_big_number import find_big

class FindBigNum(unittest.TestCase):
    def test_num(self):
        num = find_big(1, 2, 3)
        print(num)
        self.assertEqual(num, 3)
        
unittest.main()