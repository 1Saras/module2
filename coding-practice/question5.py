# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:55:39 2019

@author: saras
"""

import string

#print(string.ascii_uppercase)
#
##Task 1
#for char in string.ascii_uppercase:
#    print(char)


#Task 2
alphabet = string.ascii_uppercase
#indexs = range(0,len(alphabet))
#def count_three(alphabet):
#    letter = -1
#    for char in alphabet:
#        letter +=3
#        if letter +=3:
#            print(alphabet.lower())
            
            
for i in range(0,len(alphabet)):
    if i %3==2:
        print(alphabet[i].lower())    
    else:
        print (alphabet[i])
#    
#    print ('index',i,'with',alphabet[i] )
    
    

