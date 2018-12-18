# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:35:57 2018

@author: saras
"""
import random

def guess():
    print ("Welcome to the game!")
    guess = input("Two dice will be rolled and their sum will be odd or even. Type your guess. If you would like to leave the game type quit: " ).title()
     
    dice_value1 = random.randint(1,6)
    print("dice_value1", dice_value1)
    dice_value2 = random.randint(1,6)
    print("dice_value2", dice_value2)
    dice_val = dice_value1 + dice_value2
    print ("total dice value", dice_val)
    if dice_val %2==0:
        Answer = "Even"
    else:
        Answer = "Odd"
    print ("The answer is here", Answer) 
    print ("The guess is here", guess)      
    
    if guess== Answer:
        print("Well done - it's a match!!")
    else:
        print("Sorry - wrong guess")
    


        
#from random import randint
#def guess(counter,end_range):
#    number = randint(1,end_range)
#    print ("Welcome! Can you guess my secret number?")
#    while counter >0:
#        guess = int(input("What is your guess, choose a number between 1 and "+ str(end_range)+ ' : '))
#        if guess==number:
#            print ("Well done - your guess is correct! Goodbye")
#            break
#        elif guess >number:
#            print ("Your guess is too high")
#        elif guess <number:
#            print ("Your guess is too low. ")
#        
#        counter =counter-1
#        print ("Guesses you have left: "+ str(counter) + ' : ')
#        #removed  #
# 
#    print ("END-OF-GAME: thanks for playing!")
#    
#guess(3,20)
    