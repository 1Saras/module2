# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:55:39 2019

@author: saras
"""

import string

#print(string.ascii_uppercase)
#
##Task 1 -Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.

#for char in string.ascii_uppercase:
#    print(char)


#Task 2 -For every third letter, write it to the console in lowercase instead.

#alphabet = string.ascii_uppercase
#indexs = range(0,len(alphabet))
#def count_three(alphabet):
#    letter = -1
#    for char in alphabet:
#        letter +=3
#        if letter +=3:
#            print(alphabet.lower())
            
#    print ('index',i,'with',alphabet[i] )
    
#Task 2 - improved

#alphabet = string.ascii_uppercase
#for i in range(0,len(alphabet)):
#    if i %3==2:
#        print(alphabet[i].lower())    
#    else:
#        print (alphabet[i])
        
#Task 3 - For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4').

#alphabet = string.ascii_uppercase
#for i in range(0,len(alphabet)):
#    if i %4==3:
#        print(i+1)    
#    else:
#        print (alphabet[i])    
        
#Task 4 - If a letter satisfies both rules 2 and 3, write out its numeric position followed by the letter in lowercase (e.g. 'L' should be output as '12l').

alphabet = string.ascii_uppercase
for i in range(0,len(alphabet)):
    if i %3==2 or i %4==3:
        print((i+1) + (alphabet[i].lower()))