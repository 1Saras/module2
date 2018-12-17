# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:36:11 2018

@author: saras
"""
phonebook = {}

def input_classmates_phonebook(phonebook):

   classmate1 = input("What's your first name? ")
   phone = input("What are the last 3 digits of your phone number? ")
   lucky = input("What is your lucky number? ")
   postcode = input("What is your postcode? ")
   city = input("What is your town or city? ")

   phonebook[classmate1] = (phone, lucky, postcode, city)

   user_choice = input("Would you like to add another user? Please type yes or no ")
   if user_choice == "yes":
       phonebook = input_classmates_phonebook(phonebook)
       return(phonebook)
   else:
       return(phonebook)

phonebook = input_classmates_phonebook(phonebook)
print(phonebook)

f=open("dictionary.txt", "w+")
f.write(str(phonebook))
f.close()

##Challenge A:#
#print(sorted(phonebook))
#print(sorted(phonebook.items(), key=lambda kv:kv[1][3]))
#print(sorted(phonebook.items(), key=lambda kv:kv[1][1]))

##Challenge B:#
#  
#
#