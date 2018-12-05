# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:02:27 2018

@author: saras
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:20:54 2018

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
 
class SuperAnimal():
    
    def __init__(self,name,age):
        #this class contains 4 objects#
        self.name = name
        self.age = age
        
        self.o1 = Dog() #o1 is object number#
        self.o2 = Pug()
        self.o3 = Cat()
        self.o3 = Siamese()
        
    def playGame(self):
        print('chasing birds')
        
    def bark(self):
        return self.o1.bark()
    
    def size(self):
        return self.o2.size()
    
    def meow(self):
        return self.o3.meow()
    
    def eye_color(self):
        return self.o4.eye_color()
       
#Snoopy = Dog('Snoopy the fantastic Dog', 4)
#Snoopy.eat()
#Snoopy.bark()
#
#Felix = Cat('Felix from cat food ad', 6, 'playing with yarn')
#Felix.eat()
#Felix.meow()
#
#Doug = Pug('Wonderful Doug', 8)
#Doug.size()
#
#Sammy = Siamese('Super market Sammy', 2, 'short')
#Sammy.eye_color()


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

