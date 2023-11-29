# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:41:38 2023

@author: User
"""
# # 14-dars Dictionary

# # 1-part
# otam = {
#         'ism':'nazirov kamol',
#         't_yil': 1971,
#         'kasb':'businessman'
#         }

# print(f"Mening dadamning ismi {otam['ism'].title()}. \
# Dadam {otam['t_yil']}-yilda tug'ilganlar va ular {otam['kasb']}lar")


# onam = {
#         'ism' : 'nazirova mashxuraxon',
#         't_yil' : 1973,
#         'kasb' : 'hamshira'
#         }
# print(f"Mening onamning ismlari {onam['ism'].title()} \
# va {onam['t_yil']}-yilda tug'ilganlar. Ular {onam['kasb']} bo'lib ishlaydilar")



# # 2-part
# taomlar = {
#     "onam":"lag'mon",
#     "dadam" :"sho'rva",
#     'akam': "kabob",
#     'opam' : "osh"
#     }
# print(f"Mening onamning yoqtirgan taomi {taomlar['onam']}")
# print(f"Mening dadamning yoqtirgan taomi {taomlar['dadam']}")
# print(f"Mening akamning yoqtirgan taomi {taomlar['akam']}")
# print(f"Mening opamning yoqtirgan taomi {taomlar['opam']}")


 
# # 3-part 1st method
# python_words = {
#     'if':'agar',
#     'string':'matn',
#     'project':'proyekt',
#     'computer programme':'komputer dasturi',
#     'system':'sistema',
#     'language':'til',
#     'list': "ro'yxat"
#     }

# key = python_words.get(input("istalgan so'zni kiriting\n>>"),"Bunday so'z lug'atimizda hozircha mavjud emas")
# print(key)


# # 4 2nd method
# python_words = {
#     'if':'agar',
#     'string':'matn',
#     'project':'proyekt',
#     'computer programme':'komputer dasturi',
#     'system':'sistema',
#     'language':'til',
#     'list': "ro'yxat"
#     }

# key = input('istalgan so\'zni kiriting').lower()
# tarjima = python_words.get(key)

# if tarjima == None:
#     print('Bunday so\'z mavjud emas')
# else:
#     print(tarjima)









