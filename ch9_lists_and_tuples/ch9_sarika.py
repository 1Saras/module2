# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:04:33 2018

@author: saras
"""
##Task 1 - create a list#
my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]
print (x[0]) #this
print (x[1]) #55
print (x[2]) #that
print (x[3]) #[['apple', 'orange', 'banana']
print (x[3][0]) #apple
print (x[4]) #IndexError: list index out of range


##Task 2 - modify the list#
x.remove(my_favourite_fruits)
print(x) #['this', 55, 'that']

x[1] = 'and'
print(x) #['this', and, 'that']

x.append('again')
print(x) #['this', 'and', 'that', 'again']


##Task 3 - Slicing a list#
x=['this', 'and', 'that', 'once', 'again']
print(x[1:4]) #['and', 'that', 'once']


##Task 4 - Sorting a list#
x = [7,11,3,9,2]
y = sorted(x)
print(y) #[2, 3, 7, 9, 11]
print(x) #[7, 11, 3, 9, 2]
(x.sort()) 
print(x) #[2, 3, 7, 9, 11]

x = [7,11,3,9,2]
print(sorted(x)) #[2, 3, 7, 9, 11]
print(sorted(x,reverse=True)) #[11, 9, 7, 3, 2]
#
#
###Task 5 - Create tuple and compare with list#
#
##List example: list is mutible, so 9 is deleted##
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[-1]
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
#
###Tuple example : tuple is immutable so will be an error#
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
del b[-1]
print(b) #TypeError: 'tuple' object doesn't support item deletion

#List example: list is mutible, can assign a new value to an existing list##
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0] = 50
print(a) #[50, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Tuple example: tuple is imutible, can't assign a new value to an existing tuple##
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b[0] = 50
print(b) #TypeError: 'tuple' object does not support item assignment

#List example - adds z to the end of the list#
a = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.append('z')
print(a) #[50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'z']

#Tuple example - produces error as tuples are immutable!!#
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b.append('z') 
print(b) #AttributeError: 'tuple' object has no attribute 'append'



##Task 6 - Lambda function to sort list#
a = [3,5,80,'chocolate']
b = [5,7,10,'lasagna']
c = [1,3,7,'ice cream']
z3 = [(12,'x',5, a),(7,'h',9,b), (29,'s',6,c)]

z3 = sorted(z3, reverse = True)
print(z3)
#[(29, 's', 6, [1, 3, 7, 'ice cream']), (12, 'x', 5, [3, 5, 80, 'chocolate']), (7, 'h', 9, [5, 7, 10, 'lasagna'])]

z3 = sorted(z3)
print(z3)
#[(7, 'h', 9, [5, 7, 10, 'lasagna']), (12, 'x', 5, [3, 5, 80, 'chocolate']), (29, 's', 6, [1, 3, 7, 'ice cream'])]

z3 = sorted(z3, key=lambda s:s[2]) 
print(z3)
#[(12, 'x', 5, [3, 5, 80, 'chocolate']), (29, 's', 6, [1, 3, 7, 'ice cream']), (7, 'h', 9, [5, 7, 10, 'lasagna'])]
 



