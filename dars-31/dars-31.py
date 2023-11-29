# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:07:27 2023

@author: Avazkhon
"""
'''
Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar
qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid 
xususiyatlar qo'shing. Klassga oid xususiyatlar bilan ishlash uchun maxsus
 @classmethod lar yozing
'''

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __shaxs_num = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__user_name = ''
        Shaxs.__shaxs_num +=1

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def get_user_name(self):
        return self.__user_name
    
    def set_user_name(self, username):
        self.__user_name = username
    @classmethod
    def get_shaxslar_soni(cls):
        return cls.__shaxs_num
shaxs1 = Shaxs('ali', 'olimov', 'av244565', 2000)

    
class Talaba(Shaxs):
    """Talaba klassi"""
    __Talaba_no = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.__cars = []
        Talaba.__Talaba_no +=1
        
    @classmethod
    def get_talabalar_soni(cls):
        return Talaba.__Talaba_no
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def add_car(self, car_name):
        self.__cars.append(car_name)
    def remove_car(self, car_name):
        for x in self.__cars:
            if car_name == x:
                self.__cars.remove(x)
            else:
                print("Talabada bundan mashina yo'q")
    def get_cars(self):
        num = 1
        if self.__cars == True:
            for car in self.__cars:
                print(f"{num}. {car}")
                num+=1
        else:
            print("talabada mashina yo'q")
                
                
talaba1 = Talaba('ali', 'olimov', 'ab123', 2000, 43567)


