# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:04:33 2018

@author: saras
"""

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]
print (x[1])
print (x[2])

x.remove(my_favourite_fruits)
print(x)

x[1] = 'and'
print(x)
#
x.append('again')
print(x)
#
x.append('hello')
print(x)

x = ['the', 'cat', 'sat'] 
y = ['on', 'the', 'mat'] 
z = x + y 
print(z)
#
set(x+y)
#
print(z)
#
print(z*3)
#
x=['this', 'and', 'that', 'once', 'again']

x[1:4]

x[0:2]

x[3:5]

x[1:3]

x[-3:-1]

x = [7,11,3,9,2]
y = sorted(x)
print(y)
x.sort()
print(x)
print(x.sort())

#assigning the list to x#
x = [7,11,3,9,2]
#sorting list 
sorted(x)
sorted(x,reverse=True) 

x = [7,11,3,9,2]
x.sort()
x
x.sort(reverse=True)
x
#
#print('-----generic sorted() function------')
x = ['ab', 'bs', 'yw', 'zs', 'hd']
y = sorted(x)
print('now x is:', x)
print('now y is:', y)
print()
#
print('-----object.method .sort()-----')
x.sort()
y=x.sort()
print('now x is:', x)
print('now y is:',y)
#
#
#print('-----generic reverse sorted() function------')
#x = ['ab', 'bs', 'yw', 'zs', 'hd']
#y = sorted(x,reverse=True)
#print('now x is:', x)
#print('now y is:', y)
#print()
#
#
#print('-----object.method reverse .sort()-----')
#x.sort(reverse=True)
#y=x.sort(reverse=True)
#print('now x is:', x)
#print('now y is:',y)

##can do a True False statement to check if your guess is correct##
#z = sorted(x,reverse=True)
#if x == y:
#    print(True)
#else:
#    print(False)
#
##List example 1: list is mutible, so 9 is deleted##
#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#del a[-1]
#print(a)
#
##Tuple example 2: tuple is immutable so will be an error#
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#del b[-1]
#print(b)
#
##List example 2#
#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#a[3] = 50
#print(a)
#
##Tuple example 2#
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b[3] = 50
print(b)
#
##List example 3 - adds z to the end of the list#
a.append('z')
print(a) 
#
##Tuple example 3 - produces error as tuples are immutable!!#
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b.append('z') 
print(b)