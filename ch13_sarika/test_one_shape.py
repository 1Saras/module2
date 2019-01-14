# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:10:31 2018

@author: Sara
"""

from MovingShapes import *
frame = Frame()
shape1 = Square(frame,100)
for i in range(40):
    shape1.moveTick()
    
