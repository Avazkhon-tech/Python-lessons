# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:59:30 2023

@author: Avazkhon
"""
'''
Task No1
Avto degan yangi klass yarating. 
Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
(model, rang, korobka, narh va hokazo) qo'shing. 
Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
'''

'''
Task No2
Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
'''

'''
Task No3
Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
'''

class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.km = 0
    def get_info(self):
        return (f"Mashina haqida ma'lumtotlar: Model: {self.model}, rang: {self.rang}, karobka: {self.korobka}, narh: {self.narh}$, km: {self.km}")
    def update_km(self, km):
        self.km +=km
    def set_narh(self, yangi_narh):
        self.narh = yangi_narh
    def set_rang(self, yangi_rang):
        self.rang = yangi_rang
avto1 = Avto('gentra', 'oq', 'avtomat', 20000)
