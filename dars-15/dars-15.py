# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:51:36 2023

@author: User
"""
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}


# for key, value in sorted(python_words.items()):
#     print(f'{key} ning tarjimasi: {value}')
    
    
# people = {
#     'avazxon': 20,
#     'sardor': 22,
#     'anvar': 23,
#     'gani': 18
#     }


# for name, age in sorted(people.items()):
#     print(f"{name.title()}ning yoshi {age}da")
    


# countries = {
#     'afghanistan': 'kabul',
#     'nepal':'kathmandu',
#     'china':'beijing',
#     'georgia': 'tibilisi'
#     }

# print("Dunyodagi davlar: ")
# for country in sorted(countries):
#     print(country.upper()) 
    
    
# print('\nDavlarlarning poytaxtlari')
# for capital in sorted(countries.values()):
#     print(capital.title())

# country = input('istalgan davlatning nomini kirgazing: \n>>').lower()
# capital = countries.get(country)
# if capital==None:
#     print("Bizda bunday ma'lumot mavjud emas")
# else:
#     print(f"{country.title()}ning poytaxti {capital}")
    

# menu = {
#         'mastava' : 12000,
#         'kochaosh' : 12000,
#         'lagmon' : 13000,
#         'dum shurva' : 18000,
#         'teftel shurva' : 15000,
#         'qiyma kabob' : 10000,
#         'burda kabob': 15000   
#         }

# print("3 ta taom buyurtma bering")
# buyurtmalar = []
# for n in range(3): 
#     buyurtmalar.append(input(f'{n+1}-toam: ').lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma}ning narxi {menu[buyurtma]} so'm")
#     else:
#         print(f"bizda {buyurtma} yo'q")