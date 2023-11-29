# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:46:30 2023

@author: User
"""

# # 1
# def yosh_hisobla(ism, tugilgan_yil, joriy_yil=2023):
#     """Foydalanuvchi ismi va yoshini so'rab,
#     uning tug'ilgan yilini hisoblaydigan funksiya."""
#     print(f"Hurmatli {ism.title()}, sizning yoshingiz {joriy_yil-tugilgan_yil}da")
    
       
# ism = input('Ismingizni kiriting: ')
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tugilgan_yil=tyil, ism=ism)

# # 2
# def kvkub_hisobla(son):
#     """Foydalanuvchidan son olib,
#     uning kvadrati va kubini konsolga 
#     chiqaruvchi funksiya."""
    
#     print(f"{son} ning kvadrati: {son**2}\n"
#           f"{son} ning kubi: {son**3}")

# number = int(input("Istalgan raqamni kiriting:\n>>>"))
# kvkub_hisobla(son = number)

# # 3
# def determine_even_or_odd(son):
#     """Foydalanuvchidan son olib, 
#     son juft yoki toqligini konsolga chiqaruvchi funksiya."""
#     if son%2 == 0:
#         print(f"{son}-> juft son")
#     else:
#         print(f"{son}-> toq son")
            
# son = int(input('Istalgan sonni kiriting: \n>>>'))
# determine_even_or_odd(son = son)


# # 4
# def son_taqqosla(a, b):
#     """Foydalanuvchidan ikkita son olib, 
#     ulardan kattasini konsolga chiqaruvchi funksiya. 
#     Agar sonlar teng bo'lsa "Sonlar teng" degan xabar chiqadi"""
#     if a > b :
#         print(f"{a}>{b}")
#     elif a < b:
#         print(f"{a}<{b}")
#     else:
#         print(f"{a}={b}")   
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son_taqqosla(a = son1, b = son2)

# # 5
# """Foydalanuvchidan x va y sonlarini olib,
# x^y ni konsolga chiqaruvchi funksiya."""
# def kv_hisobla(x, y = 2):
#     """Foydalanuvchidan x va y sonlarini olib,
#     x^y ni konsolga chiqaruvchi funksiya."""
#     print(f"{son} ning kvadrati: {x**y}")
# son = int(input('istalgan sonni kiriting: \n>>'))   
# kv_hisobla(x = son)    

# # 6
# def qoldiq_tekshir(son):
#     """Foydalanuvchidan son qabul qilib, 
#     sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz 
#     bo'linishini tekshiruvchi funksiya yozing."""
#     for n in range(2,11):
#         if  son%n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
# son = int(input("son kiriting: \n>>"))
# qoldiq_tekshir(son=son)
