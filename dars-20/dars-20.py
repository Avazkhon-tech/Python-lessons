# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:22:39 2023

@author: User
"""

# # 1
# """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,
#  email manzili va telefon raqamini qabul qilib,
#  lug'at ko'rinishida qaytaruvchi funksiya yozing. 
#  Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling 
#  (masalan, tel.raqam, el.manzil)"""
 
# def user_info(ism, familiya, t_yil, t_joy, email='', yosh=None):
#     info = {'ism': ism,
#             'familiya': familiya,
#             "tug'ilgan yili" : t_yil,
#             "tug'ildan joyi" : t_joy,
#             "email" : email,
#             "yoshi" : yosh
#             }
#     return info
# user_malumot = []
# while True:
#     print('quyidagi malumotlarni kirgazing: ')
#     ism = input('ism:')
#     familiya = input('familiya: ')
#     t_yil = int(input("tug'ilgan yil: "))
#     t_joy = input("tug'ilgan joy:")
#     email = input('email')
#     yosh = input("yosh: ")
#     user_malumot.append(user_info(ism, familiya, t_yil, t_joy, yosh=''))
#     repeat = input("davom etasizmi? (yes/no)")
#     if repeat == 'no':
#         break
# print('Foydalanuvchilar haqida ma\'lumot: ')
# for user in user_malumot:
#     print(f"{familiya.title()} {ism.title()}, {yosh} yoshda, email: {email} ")

      
# # 2
# """Uchta son qabul qilib, 
# ulardan eng kattasini qaytaruvchi funksiya yozing"""

# def kattasini_aniqla(a,b,c):
#     if a>b and a>c:
#         print(f"{a} eng katta son")
#     elif b>a and b>c:
#         print(f"{b} eng katta son")
#     else:
#         print(f"{c} eng katta son")
# kattasini_aniqla(100, 40, 30)



# def kattasini_aniqla(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max
# katta = kattasini_aniqla(100, -50, -10)
# print(katta)

# """Foydalanuvchidan aylaning radiusini qabul qilib olib, 
# uning radiusini, diametrini, perimetri va yuzini lug'at 
# ko'rinishida qaytaruvchi funksiya yozing"""

# def circle_info(radius, pi=3.14):
#     aylana = {'radius' : radius,
#               'diametri' : radius*2,
#               'perimetri' : radius*2*pi,
#               'yuzi' : pi*radius**2
#               }
#     return aylana

# radius = int(input("aylana radiusini kiriting: "))
# calculation = circle_info(radius)  
# print(calculation)
# for key, value in calculation.items():
#     print(f"{key}: {value}"
#           )

# """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
# yozing (tub sonlar — faqat birga va o'ziga qoldiqsiz bo'linuvchi, 
# 1 dan katta musbat sonlar)"""

# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         flag = True
#         if n == 1:
#             flag = False
#         elif n==2:
#             flag= True
#         else: 
#             for x in range(2,n):
#                 if n%x == 0:
#                     flag = False
#         if flag:
#             tub_sonlar.append(n)
#     return tub_sonlar
# tub_sonlar_royhati = tub_sonlar_top(10, 100)
# print(tub_sonlar_royhati)



# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     c = 0
#     if n<=0:
#         print('please, enter a number greater than zero')
#     else:
#         for i in range(c,n):
#             print(c, end=' ')
#             n1 = n2
#             n2 = c
#             c = n1 + n2
# num = int(input('nechchita fibonacci raqamini bilmoqchisiz?: '))   
# fibonacci(num)

    
                    
        
            
            

    
























