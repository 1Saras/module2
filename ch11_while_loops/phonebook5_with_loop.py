# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:13:04 2018

@author: saras
"""

def input_classmates_phonebook(phonebook):
   
   counter = 0
   while counter <4:
       classmate1 = input("What's your first name? ")
       phone = input("What are the last 3 digits of your phone number? ")
       lucky = input("What is your lucky number? ")
       postcode = input("What is your postcode? ")
       city = input("What is your town or city? ")
       phonebook[classmate1] = (phone, lucky, postcode, city) 
#don't forget to put the above line inside the while loop/function. Previously this line was underneath and so was wiping out the previous input#
                
       counter = counter + 1
       if counter ==4:
           print ("Thanks and goodbye")
           break
       
   return phonebook

phonebook = {}  
phonebook = input_classmates_phonebook(phonebook)


f=open("dictionary.txt", "w+")
f.write(str(phonebook))
f.close()