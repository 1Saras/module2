# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:29:32 2018

@author: saras
"""

def inputname():
    print ("What's your first name? ")
    name = input()
    return name
    
def inputphone():
    print ("What are the last 3 digits of your phone number? ")
    phone = input()
    return phone

def inputlucky_no():
    print ("What is your lucky number? ")
    lucky_no = int(input())
    return lucky_no

def inputpostcode():
    print ("What is your postcode? ")
    postcode = input()
    return postcode

def inputcity():
    print ("What is your town or city? ")
    city = input()
    return city

def phonebookinput(classmates,counter):  
    name = inputname()
    phone = inputphone()
    lucky = inputlucky_no()
    postcode = inputpostcode()
    city = inputcity()
    classmates[name] =(phone, lucky, postcode, city)
    if counter<4 : #counter is miscounting#
        counter =counter +1     
        print(counter)
        classmates = phonebookinput(classmates,counter) 
        
    else:
        print(classmates)
    return classmates
   
classmates = {}

counter = 0

classmates=phonebookinput(classmates,counter)

# -------A simpler and shorter way to do this is:-----------# 
#def phonebookinput(classmates):  
#    name = input("What's your first name? ")
#    phone = input("What are the last 3 digits of your phone number? ")
#    lucky = input("What is your lucky number? ")
#    postcode = input("What is your postcode? ")
#    city = input("What is your town or city? ")
#    classmates[name] =(phone, lucky, postcode, city)
#    print(classmates)
#    return classmates
#
#classmates = {}
#classmates = phonebookinput(classmates)
#
#phonebookinput(classmates)  
    