# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:02:27 2018

@author: saras
"""

class Animal():
    def __init__(self, age=0):
        self.age = age
        
    def eat(self):
        print('yum yum yum!')

class Dog(Animal):
    def __init__(self, age=0, barkNumber=0):
        self.barkNumber = barkNumber

    def bark(self):
        print('Woof! '*self.barkNumber)
        
class Pug(Dog):
    def size(self):
        print('small')
        
class Cat(Animal):
    def meow(self):
        print('Meow!')
        
                
Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

Felix = Cat()
Felix.meow()
Felix.eat()

Doug = Pug()
Doug.size()


#class Robot():
#    def move(self):
#        print('...move move move...')
#class CleanRobot(Robot):
#    def clean(self):
#        print('I vacuum dust')
#class CookRobot(Robot):
#    def cook(self):
#        print ('I make rice')
#        
#Robbie = Robot()
#Robbie.move()

