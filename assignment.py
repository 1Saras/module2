# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:56:44 2018

@author: saras
"""

class Person:
    def __init__(self):
        self.name = None
        self.age = 'not defined'
        self.isMale = None

p1 = Person()
p1.age

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised!')
 
    def greetingInformal(self):
        print('Hi', self.name)
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.name)
        else:
            print('Welcome, Ms', self.name)
 
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young ', self.name)
        elif self.age > 60:
            print('Welcome, venerable ', self.name)
        else:
            self.greetingFormal()

      
p1 = Person('John',44,'m')
p1.name

p1.isMale

p1 = Person('Harry',12,'m')
p2 = Person('Jean',12,'f')
p3 = Person('Richard',50,'m')


p1.greetingInformal()
p1.greetingFormal()
p2.greetingFormal()
p1.greetingAgeBased()
p2.greetingAgeBased()
p3.greetingAgeBased()


 