# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 21:15:23 2023

@author: Avazkhon
"""
'''
Task No1
Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
'''

'''
Task No2
Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
'''

'''
Task No3
Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
'''

'''
Task No4
Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
'''

'''
Task No5
dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi 
turli klass va obyektlarning xususiyatlari va 
metodlarini toping (dir(str),dir(int) va hokazo)
'''

class Avtosalon:
    def __init__(self, salon_nomi, manzil, sotuvdagi_avtomobillar):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.sotuvdagi_avtomobillar = sotuvdagi_avtomobillar
    def get_info(self):
        return(f"Salon nomi: {self.salon_nomi}, manzil: {self.manzil}, sotuvdagi mashinalar: {self.sotuvdagi_avtomobillar}")
        
    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith("__") is False]        
        
    
salon1 = Avtosalon("driver's village", 'qoqon shahar', 'gentra')
salon1_dict = salon1.__dict__
for key, value in salon1_dict.items():
    print(f"{key}: {value}")

