# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:52:47 2023

@author: User
"""

import datetime as dt
today = dt.date.today()
my_birthday = dt.date(2003, 12, 29)
difference = today - my_birthday 
kunlar = difference.days
oylar = round(kunlar/30)
yillar = round(oylar/12)
print(f"Kunlar: {kunlar}")
print(f"Oylar: {oylar}")
print(f"Yillar: {yillar}")