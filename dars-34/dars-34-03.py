# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:09:36 2023

@author: User
"""

"""
Faylda 3 ta talabaning ism va familiyasi saqlangan. 
Ularning har birini alohida qatordan "Ism Familiya, n-kurs, 
Fakultet talabasi" ko'rinishida konsolga chiqaring.
"""
import json
with open('students.json') as f:
    data = json.load(f) 
print(data)

for item in data['student']:
    print(f"{item['name']} {item['lastname']}, {item['year']}-kurs, {item['faculty']} fakulteti talabasi")