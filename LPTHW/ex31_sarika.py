# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:05:23 2018

@author: Sara
"""
print ("You enter a dark room with two doors. Do you go through door #1, door #2 or door #3?")

door = input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print ("The bear eats your face off. Good job!")
    elif bear == "2":
        print ("The bear eats your legs off. Good job!")
    else:
        print ("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print ("You stare into the endless abyss at Cthulhu's retina.")
    print ("1. Blueberries.")
    print ("2. Yellow jacket clothespins.")
    print ("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print ("Your body survives powered by a mind of jello. Good job!")
    else:
        print ("The insanity rots your eyes into a pool of muck. Good job!")


elif door == "3":
    print ("What do you think of this story?")
    print ("1. It's so crazy I love it!")
    print ("2. It's so strange what is the author on?!")
    
    opinion = input("> ")
    
    if opinion == "1":
        print ("Ha ha you are just as crazy as the author - go home and get some rest!")
    elif opinion == "2":
        print ("Plot twist- you are the author mwahhhhaaa!!!")
    else: 
        print ("Ah you are one of those who sits on the fence - that must hurt") 

else:
    print ("You stumble around and fall on a knife and die. Good job!")