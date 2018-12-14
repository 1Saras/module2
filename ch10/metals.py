# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:09:04 2018

@author: saras
"""

metals = {'iron':(7.8, 12.5, 498), 'gold':(19.3, 32.1, 230), 'zinc':(7.13, 84.8, 879), 'lead':(11.4, 98.1, 384)}
print(metals)

metals_keys = list(metals.keys())

print(sorted(metals.items(), key=lambda kv:kv[1][1]))

print(sorted(metals.items(), key=lambda kv:kv[1][1],reverse=True))

metals_keys.sort(key=lambda k:metals[k][1],reverse=True)
print (metals_keys)