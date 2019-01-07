# -*- coding: utf-8 -*-/.
"""
Created on Sun Dec 16 13:57:56 2018

@author: Sara
"""
from Shapes import *
from pylab import random as r
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        
        self.figure = Shape(shape,diameter)
              
        self.dx = 5 + 10 * r() #07/6 rate of movement, amended from 10#
        self.dy = 5 + 10 * r() #07/6 rate of movement, amended from 10#
        
        def calculate_min_max(self,frame):
            d = self.diameter
            self.minx = d/2.0 #min x start position
            self.maxx = frame.width-d/2.0 #max x start position so that the shape stays in the frame
            self.miny = d/2.0 #min y start position
            self.maxy = frame.height-d/2.0 #max y start position so that the shape stays in the frame
        calculate_min_max(self,frame)
                    
        self.x =  self.minx + r() * (self.maxx - self.minx) #07/5 starting position#
        self.y = self.miny + r() * (self.maxy - self.miny) #07/5 starting position#
        
        #stuck on where and how to put r() < 0.5 (question 7/7) - adds random variation for the start positions
          
        
    def goto(self,x,y): #added then removed the 0's#
        self.figure.goto(x,y)
        
        
    def moveTick(self):
#        self.x = self.x  
#        self.y = self.y  
        
        if self.x > self.maxx:
            self.dx = self.dx*-1
        if self.x < self.minx:
            self.dx = self.dx*-1
        if self.y > self.maxy:
            self.dy = self.dy*-1
        if self.y < self.miny:
            self.dy = self.dy*-1
            
        self.x = self.x + self.dx #07/5 adds animation
        self.y =self.y + self.dy #07/5 adds animation
        
        self.goto(self.x, self.y) #added this#
        
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        def calculate_min_max(self,frame):
            d = self.diameter
            self.minx = d/2.0 #min x start position
            self.maxx = frame.width-d/2.0 #max x start position so that the shape stays in the frame
            self.miny = d/2.0 #min y start position
            self.maxy = frame.height-d/2.0 #max y start position so that the shape stays in the frame
        calculate_min_max(self,frame)
        
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)

#stuck on part 7/9 - hitting the wall. The below is incorrect. Also the other shapes bounch but still go slightly past the wall
#        diameter2 = 2*diameter
#
#        self.minx = diameter2
#        self.maxx = frame.width-(diameter2)
#        
#        self.miny = diameter2
#        self.maxy = frame.height-(diameter2)
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
        