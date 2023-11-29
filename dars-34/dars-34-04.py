# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:29:23 2023

@author: User
"""

import json
with open('wikipedia.json') as f:
    wiki = json.load(f)
title = wiki['query']['pages']['13801']['title']
extract = wiki['query']['pages']['13801']['extract']
print(title)
print(extract)