# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:57:55 2023

@author: User
"""

ismlar = ['Anvar', "G'ani", "Toshmat"]
print("Salom " + ismlar[0] + ", uyga vazifam bilan yordam bera olasanmi?") 
print("Ishlaring yaxshimi " + ismlar[1]+ "?")
print(f"{ismlar[1]} va {ismlar[2]} inoq do\'stlar")
print(ismlar[1], "va", ismlar[2], "inoq do'stlar")


#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [100, 200, 300, 400, -200, 44.5]

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar[0] = sonlar[0] - sonlar[4]
sonlar[0] = 100
del sonlar[0]
sonlar.insert(0, 100)


t_shaxslar = ["Amir Temur", "Beruniy", "Xorazmiy"]
z_shaxslar = ["Steve Jobs", "Warren Buffet", "James Bond"]
print("Men ", t_shaxslar[0], "haqida kitoblar uqishni yoqtiraman" )
print("Men ", z_shaxslar, "bilan suhbat qurishni xohlayman")

friends = []
friends.append("Jasur")
friends.append("Akmal")
friends.append("Shoxruh")
friends.append("Ahmad")
friends.append("Bobur")
friends.insert(0, 'Hasan')
friends.insert(-1, "Teshavoy")
friends.remove('Jasur')
friends.remove('Ahmad')

mehmonlar = []
mehmonlar = friends.pop(0)
mehmonlar = friends.pop(2)
mehmonlar = friends.append("Ali")
