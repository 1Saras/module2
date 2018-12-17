# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:09:04 2018

@author: saras
"""

metals = {'iron':(7.8, 12.5, 498), 'gold':(19.3, 32.1, 230), 'zinc':(7.13, 84.8, 879), 'lead':(11.4, 98.1, 384)}
print(metals)

#turns the tuples into lists#
metals_keys = list(metals.keys())
#
#sorts by share price accending#
print(sorted(metals.items(), key=lambda kv:kv[1][1]))

##sorts by share price in reverse order#
#print(sorted(metals.items(), key=lambda kv:kv[1][1],reverse=True))
#
##sorts by share price in reverse order but only showing the keys#
#metals_keys.sort(key=lambda k:metals[k][1],reverse=True)
#print(metals_keys)

#sorting by experiment ascending#
#print(sorted(metals.items(), key=lambda kv:kv[1][2]))
#sorted(densities, reverse=True,key=lambda m:densities[m] [1] [0])
sorted(metals.items(),key=lambda kv:kv[1][1],reverse=True)
sorted(metals.items(),key=lambda kv:kv[1][1],reverse=True)[2]

