# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:44:24 2023

@author: User
"""

import unittest
from people import Shaxs, Talaba

# class ShaxsTest(unittest.TestCase):
#     def setUp(self):
#         ism = 'Avazxon'
#         familiya = 'Nazirov'
#         passport = 'AA1234567'
#         tyil = 2000
#         self.person1 = Shaxs(ism, familiya, passport, tyil)
#     def test_create(self):
#         self.assertIsNotNone(self.person1.ism)
#         self.assertIsNotNone(self.person1.familiya)
#         self.assertIsNotNone(self.person1.passport)
#         self.assertIsNotNone(self.person1.tyil)
    
#     def test_get_info(self):
#         new_info = 'Avazxon Nazirov. Passport:AA1234567, 2000-yilda tug`ilgan'
#         self.assertEqual(new_info, self.person1.get_info())
        
#     def test_get_age(self):
#         age = 23
#         self.assertEqual(age, self.person1.get_age(2023))
#     def test_get_name(self):
#         name = 'Avazxon'
#         self.assertEqual(name, self.person1.get_name())

class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = 'Avazxon'
        familiya = 'Nazirov'
        passport = 'AA1234567'
        tyil = 2000
        idraqam = 12345
        self.bosqich = 1
        self.person1 = Talaba(ism, familiya, passport, tyil, idraqam)
    def test_create(self):
        self.assertIsNotNone(self.person1.ism)
        self.assertIsNotNone(self.person1.familiya)
        self.assertIsNotNone(self.person1.passport)
        self.assertIsNotNone(self.person1.tyil)
    def test_get_info(self):
        new_info =  'Avazxon Nazirov. 1-bosqich. ID raqami: 12345'
        self.assertEqual(new_info, self.person1.get_info())
    def test_get_id(self):
        new_id = 12345
        self.assertEqual(new_id, self.person1.get_id())
    def test_get_bosqich(self):
        self.assertEqual(self.bosqich, self.person1.get_bosqich())
    
unittest.main()
    