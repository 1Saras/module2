# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:36:11 2018

@author: saras
"""
phonebook = {}

def input_classmates_phonebook(phonebook, counter):

   classmate1 = input("What's your first name? ")
   phone = input("What are the last 3 digits of your phone number? ")
   lucky = input("What is your lucky number? ")
   postcode = input("What is your postcode? ")
   city = input("What is your town or city? ")

   phonebook[classmate1] = (phone, lucky, postcode, city)


counter = 0
while counter <4:
    print(counter)    
    input_classmates_phonebook(phonebook, counter)
    counter +=1


f=open("dictionary.txt", "w+")
f.write(str(phonebook))
f.close()

