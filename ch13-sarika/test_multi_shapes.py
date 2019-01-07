# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:43:47 2018

@author: Sara
"""

from MovingShapes import *
frame = Frame()
numshapes = 3 #creates 3 sqaures
shapes = []        
size = 60       
for i in range(numshapes):
    shapes.append(Square(frame,100))
    shapes.append(Diamond(frame,100))
    shapes.append(Circle(frame,100))    
for i in range(300):
    for shape in shapes:
        shape.moveTick()
frame.close()
#        
#for i in range(numshapes):
#    shapes.append(Square(frame,100))
#for i in range(100):
#    for shape in shapes:
#        shape.moveTick()
#frame.close() 