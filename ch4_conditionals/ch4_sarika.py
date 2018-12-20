# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Task 3 - IF statements#

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer

if number >10:
    print("Too high!")
    
if number <=0:
    print("Too low!")


##Task 4 - ELSE statements#

number = input("Enter a number between 1 and 10: ")
number = int(number)

if number >10:
    print("Too high!")
    
elif number <=0:
    print("Too low!")
    
else:
    print("Well done!!")


##Task 5 - ELIF statements#

#correct order:#

age = input("Enter age: ")
age = int(age)

if age <13:
    print('child')

elif age <18:
    print('teen')
    
elif age <65:
    print('adult')
    
else:
    print('pensioner')

#Order is important - the below will cause incorrect behaviour:#
    
age = input("Enter age: ")
age = int(age)

if age <65:
    print('adult')

elif age <13:
    print('child')

elif age <18:
    print('teen')
     
else:
    print('pensioner')
    
    
    
    
    
    
    