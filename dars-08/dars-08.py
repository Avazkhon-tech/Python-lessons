# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:25:52 2023

@author: User
"""

countries = ['South Africa', 'Greece', 'Australia', 'Norway', 'United Kingdom', 'France', 'Switzerland',]
print(len(countries))
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
countries.sort()
countries.sort(reverse=True)

sonlar_royxati = list(range(120,1201))
print(sum(sonlar_royxati))

print(max(sonlar_royxati) - min(sonlar_royxati))
print(len(sonlar_royxati))

print(sonlar_royxati[:20])
print(sonlar_royxati [-20:])


taomlar = ["Burger", "Sandwich", 'Hot Dog', 'Cheese Burger', 'Peri Peri Fries']
nonushta = taomlar[:]

nonushta.remove('Burger')
nonushta.remove('Hot Dog')
nonushta.remove('Cheese Burger')
nonushta.append('Sutli osh')
nonushta.append('Quymoq')
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
nonushta[0] = 'qaymon va non'
