# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:50:09 2023

@author: User
"""
"""Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya"""

num_list = [1,2,3,4,5,6,7,8,9,10]
def even_number_sorter(lists):
    even_num_list = []
    for num in lists:
        if num%2 == 0:
            even_num_list.append(num)
    return even_num_list