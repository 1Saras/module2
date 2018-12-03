# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:06:40 2018

@author: saras
"""

name = 'Zed A. Shaw'
age = 35 
height = 74 
weight = 180 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %s." % name)
print ("He's %d inches tall." % height)
print ("He's %d pounds heavy." % weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)

print ("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))

#write some variables that convert the inches and pounds to centimeters 
#and kilograms. Do not just type in the measurements. Work out the math in Python:#

def convert_weight(lbs):
    kilograms = (lbs * 0.45359237)
    return (lbs, kilograms)

conversion = convert_weight(180)
print (conversion)

def convert_height(inches):
    centimeters = (inches * 2.54)
    return (inches, centimeters)

conversion2 = convert_height(74)
print (conversion2)
