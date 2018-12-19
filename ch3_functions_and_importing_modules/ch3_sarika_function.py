# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:44:56 2018

@author: saras
"""

#Task 2 - First function#
def greeting():
    print ("Hello World!")
       
def introduction():
    print ("What's your name? ")
    name = input()
    print ("Hello {}!".format(name.upper()))
    print (2+2)


#Task 4 - print version#
def asking():
    print ("Please choose a number")
    numbera = input()
    print ("Please choose another number")
    numberb = input()
    print ("Here is the sum:") 
    print (int(numbera)+int(numberb))

def add_two_numbers():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))
    
def add_two_numbers_from_args(number1, number2):
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))


#Task 4 -return version#
def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer # 3
returned_value = add_two_numbers_and_return_value()
print(returned_value)
print(returned_value - 5)    

 
#Task 5 -Convert temperatre return version#
def convert_temperature(): 
    centigrade = int(input("What temperature in centigrade do you want to convert to fahrenheit and kelvin? "))
    fahrenheit = (centigrade * 9.0) / 5.0 + 32
    kelvin = centigrade + 273.15
    return (centigrade, fahrenheit, kelvin)
    print (centigrade, fahrenheit, kelvin)
