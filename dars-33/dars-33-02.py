# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:51:37 2023

@author: User
"""

with open('pi_million_digits.txt') as file:
    pi = file.read()
    pi = pi.replace('\n', '')
    pi = pi.replace(' ', '')
    pi = pi.rstrip()  
t_sana = input("Tugildan sanangizni ushbu ko'rinishda kiriting (daymonthyear => 01012000)")
if t_sana in pi:
    print("tug'ilgan kuningiz pi ning qiymati ichida mavjud")
else:
    print("tug'ilgan kuningiz pi ning qiymati ichida mavjud emas")




pi = float(pi)
import pickle
with open('pi.pkl', 'wb') as file:
    pickle.dump(pi,file)
    
