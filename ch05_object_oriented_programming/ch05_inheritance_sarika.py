# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:02:27 2018

@author: saras
"""

class Animal():
    def __init__(self, name, age=0):
        self.age = age
        self.name = name
        
    def eat(self):
        print('yum yum yum!')

class Dog(Animal):
    def bark(self):
        print('Woof! ')
        
class Pug(Dog):
    def size(self):
        print('small')
            
class Cat(Animal):
    def __init__(self, name, age=0, hobby=''):
#        Cat.__init__(self, name, age=0)    
        self.hobby = hobby 
    def meow(self):
        print('Meow!')  
        print('Cats hobby is {}' .format(self.hobby))
        
class Siamese(Cat):
    def __init__(self, name, age=0, hair=''):
        Animal.__init__(self, name, age=0)
        self.hair = hair
    def eye_color(self):
        print('bright blue')
        print('{} has bright blue eyes and {} hair'.format(self.name, self.hair))
        
Snoopy = Dog('Snoopy the fantastic Dog', 4)
Snoopy.eat()
Snoopy.bark()

Felix = Cat('Felix from cat food ad', 6, 'playing with yarn')
Felix.eat()
Felix.meow()

Doug = Pug('Wonderful Doug', 8)
Doug.size()

Sammy = Siamese('Super market Sammy', 2, 'short')
Sammy.eye_color()


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
