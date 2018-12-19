# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:18:26 2018

@author: Sara
"""
##There are different ways to debug#

##---------1. Print Function---------#

#Get the following error TypeError: unsupported operand type(s) for -: 'str' and 'int'#
#userInput = input('Please give a number ')
#result = userInput - 2
#
##Can use print function for debugging. In this case it's been used to check type. This will give the message: <class 'str'>#
userInput = input('Please give a number ')
print(type(userInput))
#
##---------2.Breakpoints---------#
#
##Double click line number of code to create breakpoint, can use the blue buttons to run code in debugging mode#
#userInput = input('Please give a number ')
#def simpleOperation(userInput):
#    intInput = int(userInput)
#    result = intInput - 2
#    return result
#def nestedOperation(result):
#    result = simpleOperation(userInput)
#    result2 = result * 2
#    return result2
#result = simpleOperation(userInput)
#result2 = nestedOperation(result)
#print(result2)

#------Avoiding key errors - the below avoids error message------#

#tel = {}
#tel = {'alf':111, 'bobby':222, 'calvin':333}
#
#tel['Martiena'] = 145
#tel['Mag'] = 281
#
##Sam is not in the directory#
#k = 'Sam'
#
#if k in tel:
#    print(k, ':', tel[k])
#    
#else:
#    print(k, 'not found!')

#Mag is in the dictionary so her data will be printed#
#k = 'Mag'
#
#if k in tel:
#    print(k, ':', tel[k])
#    
#else:
#    print(k, 'not found!')