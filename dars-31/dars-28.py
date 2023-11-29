# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 18:46:08 2023

@author: Avazkon
"""

class User:
    def __init__(self, user, ism, familiya, email, telefon_raqam, tyil):
        self.user = user
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.telefon_raqam = telefon_raqam
        self.tyil = tyil
    def get_info(self):
        print(f"Foydalanuvchi haqida ma'lumot: \n"
              f"Ism: {self.ism} \n"
              f"Familiya: {self.familiya}\n"
              f"Email: {self.email}\n"
              f"Telefon raqam: {self.telefon_raqam}\n"
              f"Tug'ilgan yil: {self.tyil}\n"
              )
    def get_info1(self):
        return (f"Foydalanuvchi: "
                f"{self.user}, "
                f"ismi: {self.ism}, "
                f"familiyasi: {self.familiya}, "
                f"email: {self.email},"
                f"telefon raqam: {self.telefon_raqam}, "
                f"tug'ilgan yili: {self.tyil}. "
              )
        
    
user1 = User('Avazxon8775', 'Avazxon', 'Nazirov', 'avazxonnazirov334@gmail.com', '+99899992****', 2000)
user2 = User('ali2000', 'Ali', 'Alijonov', "ali2020@gmail.com", '+998999999999', 2000)

user1.get_info1()
user1.get_info()
user2.get_info1()
user2.get_info()