# -*- coding: utf-8 -*-
""" 
Created on Fri Jul 28 10:13:04 2023

@author: User
"""
import re
text1 = """Assalom alaykum hurmatli do'stlar. Navbatdagi 
darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI"""

text2 = """Ushbu darsimizda unittest moduli yordamida klasslarning 
xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

andoza = "(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+"
url1 = re.findall(andoza, text1)
print(url1)
url2 = re.findall(andoza, text2)
print(url2)



    
    
    
    
    