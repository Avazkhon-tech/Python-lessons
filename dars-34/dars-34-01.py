# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:31:50 2023

@author: User
"""

"""
Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
"""
import json
data = {
        "Model" : "Malibu", 
        "Rang" : "Qora", 
        "Yil":2020, 
        "Narh":40000
        }
data_json = json.dumps(data)

with open ("data.json", "w") as f:
    json.dump(data, f)



