# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:52:42 2023

@author: User
"""
class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        return yil - self.tyil
    
class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, yillik_daromad, dukon_manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.annual_income = yillik_daromad
        self.location = dukon_manzil
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"Yillik daromad: {self.annual_income}"
        info += f"Do'kon manzili: {self.location}"
        return info
    def get_income(self):
        return self.annual_income
    def get_location(self):
        return self.location


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, marital_status):
        super().__init__(ism, familiya, passport, tyil)
        self.debt = 0
        self.marital_status = marital_status
    def get_m_status(self):
        return self.marital_status
    def get_debt(self):
        return f"Qolgan qarz {self.debt}"
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"Marital status: {self.marital_status}"
        return info
    
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, user_id):
        super().__init__(self, familiya, passport, tyil)
        self.user_id = user_id
    def get_user_id(self):
        return self.user_id
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"User id: {self.user_id}"
        return info
    
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, user_id, admin_id):
        super().__init__(ism, familiya, passport, tyil, user_id)
        self.admin_id = admin_id
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"User id: {self.user_id}"
        info += f"Admin id: {self.admin}"
        return info
        
    def get_admin_id(self):
        return self.admin_id
        
    def ban_user(self):
        print("foydalanuvchi bloklandi")
        
        
        
        
        
        
        
        