# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:25:52 2018

@author: saras
"""


##Task 1#

x = 33
while x >=1:
        print(x, ': ', end='')
        x = x / 2
print(x)        


##Task 2#

def triangular():
    n = int(input("choose a number? "))
    result = 0 
    while n > 0:
        result = result + n
        n = n-1 
    return result

print(triangular())



##Task 3#

mark = 1
while mark > 0:
    mark = int(input('Enter student mark '))
    if mark >=80:
        print("Top marks that's a first class!")
    elif mark >=60:
            print("Well done you passed!")
    else:
        print("Sorry that's a fail - you can retake in June")

i = 55
while i > 10:
    print (i)
    i = i * 0.8
    if i==35.2:
        break

##Task 4#   
while True:
    name = input("Please enter name: ")
    if name == "done":
        break
    print ("Hello", name)
    
    
##Task 5#      
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

