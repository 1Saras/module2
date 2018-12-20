# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:16:46 2018

@author: saras
"""

from random import randint
def guess(counter,end_range):
    number = randint(1,end_range)
    print ("Welcome! Can you guess my secret number?")
    while counter >0:
        guess = int(input("What is your guess, choose a number between 1 and "+ str(end_range)+ ' : '))
        if guess==number:
            print ("Well done - your guess is correct! Goodbye")
            break
        elif guess >number:
            print ("Your guess is too high")
        elif guess <number:
            print ("Your guess is too low. ")
        
        counter =counter-1
        print ("Guesses you have left: "+ str(counter) + ' : ')
        #removed  #
 
    print ("END-OF-GAME: thanks for playing!")
    
guess(3,20)