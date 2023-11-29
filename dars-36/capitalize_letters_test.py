# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:25:28 2023

@author: User
"""

import unittest
from capitalize_letters import capitalize_letters
colors = ["red", "blue", "green"]
formatted = ['Red', 'Blue', 'Green']

class CapitalTest(unittest.TestCase):
    def test_words(self):
        capitalized_words = capitalize_letters(colors)
        self.assertListEqual(capitalized_words, formatted)
unittest.main()