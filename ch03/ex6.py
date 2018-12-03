# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:16:42 2018

@author: saras
"""

#variable and value#
x = "There are %d types of people." % 10

#variable and value#
binary = "binary"

#variable and value#
do_not = "don't"

#variable and value#
y = "Those who know %s and those who %s." % (binary, do_not)

#print the string thats on line 9#
print (x)

#print the string thats on line 18#
print (y)

#print the string thats on line 9#
print ("I said: %r." % x)

#print the string thats on line 18 and 15#
print ("I also said: '%s'." % y)


#variable and value#
hilarious = False

#variable and value#
joke_evaluation = "Isn't that joke so funny?! %r"

#print string from lines 37 and 34#
print (joke_evaluation % hilarious)

#variable and value#
w = "This is the left side of..."

#variable and value#
e = "a string with a right side."

#puts together the value from lines 43 and 46#
print (w + e)