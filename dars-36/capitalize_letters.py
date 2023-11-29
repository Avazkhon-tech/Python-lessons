# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:16:55 2023

@author: User
"""

"""
Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
birinchi harfini katta harfga o'zgatiruvchi funksiya
"""

colors = ["red", "blue", "green"]
colors_capital = []
def capitalize_letters(words):
    for word in words:
        colors_capital.append(word.title())
    return colors_capital
    