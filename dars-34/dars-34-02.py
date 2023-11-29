# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:37:36 2023

@author: User
"""

'''
Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini 
konsolga chiqaring: 
    talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""    
'''
import json
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"{talaba['ism']}, {talaba['familiya']}")

with open ('talaba.json', 'w') as f:
    json.dump(talaba, f)
    