# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:52:41 2018

@author: saras
"""

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "sb", "lf", "hw", "ed", "fy"] 
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)
x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
y[0]='zz'

#print(sorted(x2, key=lambda s:s[1]))

#print(sorted(x2, key=lambda s:s[2]))
#
#print(sorted(x2, key=lambda s:s[2][1]))

#x = [1,2,3,4]
#y = [3,4,10,3]
#z = [20,10,30,40]
#
#x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
#
#print(sorted(x2, key=lambda s:s[2][-1]))
    
#y[0]='zz'
#y[-1]='jf'
#
#x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
#
#print(sorted(x2, key=lambda s:s[2][1]))
#print(sorted(x2, key=lambda s:s[2][-3]))
a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6)
c = [2,2,3,3,4,5,6,7,8,9]
myFavF = ["apple", "orange", "banana"]
x = ["lf", "sb", "hw", "aa", "ed", "fy"] 
z = ["uj", "fg", "uj", "ww", "sx", "cf"]
y = sorted(x)

y[0] ='zz'
y[-2] ='sd'

x2 = [(a, 3, 'a', z), (c, 1, 'c', y), (b, 5, 'b', x)]

 
#sorted(x2, key=lambda s:s[0][-3])
#sorted(x2, key=lambda s:s[3][-3][-2])
#sorted(x2, key=lambda s:s[3][-3][-2]) [0]





