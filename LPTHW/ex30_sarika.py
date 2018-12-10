# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#assigning values to the variables#
people = 50
cars = 30
buses = 40

#if there more cars than people then print the statement in line 14, if there are less cars than people print the statement in line 16, otherwise print the statement in line 18#
if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")

#if there more buses than cars then print the statement in line 22, if there are less buses than cars print the statement in line 24, otherwise print the statement in line 26#
if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

#if there are more people than buses print the statement in line 30, otherwise print the statement in line 32#
if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print ("Fine, let's stay home then.")

#if there are more car than people AND less buses than cars print "a" 
#if there are less cars than people AND more buses than cars print "b"
#otherwise print c
if cars > people and buses < cars:
    print ("a")
elif cars < people and buses > cars:
    print ("b")
else:
    print ("c")