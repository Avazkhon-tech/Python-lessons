# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:47:12 2023

@author: User
"""
import datetime as dt 
today = dt.date.today()
ramazon = dt.date(2024, 3, 9)
eid_al_adha = dt.date(2024, 6, 16)
difference = ramazon - today
difference2 = eid_al_adha - today


print(f'Ramazonga {difference.days} kun qoldi')
print(f'Qurbon hayitiga {difference2.days} kun qoldi')
