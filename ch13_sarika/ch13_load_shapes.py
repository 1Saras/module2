# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 11:51:51 2018

@author: Sara
"""

from Shapes import *

frame = Frame()
s1 = Shape('square', 100) #2nd argument sets figures diameter
s1.goto(200,100) #calls the figures goto method,moving it to the specified (x,
#y) coordinates

#part: 07/2 all the below creates movement
x = 0
y = 0

for i in range(100):
    x = x + 5
    y = y + 5
    s1.goto(x, y)
    
