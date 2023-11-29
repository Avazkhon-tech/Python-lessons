# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:35:54 2023

@author: User
"""

import datetime as dt
today = dt.date.today()
range1 = range(1,10)
for i in range1:
    n = i
    future = dt.date(2023, 8, n)
    print(future)