# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:18:26 2018

@author: Sara
"""
#There are different ways to debug

#---------1. Print Function---------

#Get the following error TypeError: unsupported operand type(s) for -: 'str' and 'int':
    
userInput = input('Please give a number ')
result = userInput - 2

#Can use print function for debugging. In this case it's been used to check type. This will give the message: <class 'str'>:

userInput = input('Please give a number ')
print(type(userInput))

#---------2.Breakpoints---------

userInput = input('Please give a number ')
def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result
def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2
result = simpleOperation(userInput) 
result2 = nestedOperation(result)
print(result2)

#How to use debug navigation buttons to run the breakpoint debug procedure:
#Firstly add a breakpoint at line 30: result = simpleOperation(userInput). 
#This is done by double clicking the line number of code. 
#The blue buttons are the debugging buttons:
#The first blue button starts running the code until the break point.
#The second button runs the code line-by-line until the breakpoint.
#The third button steps into sections that would to look at in more detail.
#The fourth button allows the user to step out of that code.
