# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 19:48:04 2023

@author: Avazkhon
"""

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
    def get_fan_nomi(self):
        return self.nomi
    
    
class Talaba:
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.idraqam = idraqam
        self.fanlar = []
    def fanga_yozil(self, fan):
        f = fan.get_fan_nomi()
        self.fanlar.append(f)
    def get_fan(self):
        return self.fanlar
    def remove_fan(self, x):
        for x in self.fanlar:
            if x in self.fanlar:
                self.fanlar.remove(x)
                print("fan muvaffaqiyatli o'chirildi")
            else:
                print("siz ushbu fanga yozilmagansiz")
                

maths = Fan("Matem")
pyhsics = Fan('Fizika')
biology = Fan("biologiya")
talaba1 = Talaba('avaz', 'nazirov', 'sd243', 2000, 546)
talaba2 = Talaba('jasur', 'anvarov', 'sd3456', 2001, 298)
talaba3 = Talaba('ali', 'olimov', 'sdf3454', 354, 546)




 



    













# maths = Fan("Matematika")
# pyhsics = Fan("fizika")
# biology = Fan("bialogiya")
# subject = [maths, pyhsics, biology]
# talaba1 = Talaba('Avaz', 'Nazirov', "df2345", 2000, 324, subject)

