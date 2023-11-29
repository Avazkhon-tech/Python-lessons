# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:16:47 2023

@author: User
"""

"""Berilgan son Fibonachchi ketma-ketligida uchraydimi 
(True) yoki yo'q (False) qaytaruvchi funksiya yozing."""

def fibonacci(n):
    fibonacci_list = []
    n1 = 0
    n2 = 1
    c = 0
    if n<=0:
        print('please, enter a number greater than zero')
    else:
        for i in range(c,n):
            n1 = n2
            n2 = c
            c = n1 + n2
            fibonacci_list.append(c)
    return fibonacci_list

def num_checker(value):
    if value in fibonacci(15):
        return True
    else:
        return False
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    