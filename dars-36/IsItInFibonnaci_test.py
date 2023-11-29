# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:52:58 2023

@author: User
"""

import unittest
from IsItInFibonnaci import num_checker

class Check_if_fibonacci(unittest.TestCase):
    def test_if_true(self):
        self.assertTrue(num_checker(610))
    def test_if_fale(self):
        self.assertFalse(num_checker(200))
unittest.main()
        