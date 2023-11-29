# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:57:05 2023

@author: User
"""

"""Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
def find_big(a, b, c):
    biggest_number = a
    if b>c and b>a:
        biggest_number = b
    elif c>b and c>a:
        biggest_number = c
    return biggest_number
