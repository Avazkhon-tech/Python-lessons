# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:02:43 2023

@author: User
"""

import re 
phone_num = input("Telefon taqamingizni kirting: ")
andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
while True:
    phone_num = input("Telefon taqamingizni kirting: ")
    if re.match(andoza, phone_num):
        print("Raqamizgiz qabul qilindi")
        break
    else:
        print("iltimos telefon raqam kiriting")