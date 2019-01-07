# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:59:29 2019

@author: saras
"""

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print("Gender not recognised!")
            
    def greetingInformal(self):
        print('Hi', self.name)
            
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.name)
        else:
            print('Welcome, Ms', self.name)
            
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young', self.name)
        elif self.age > 60:
            print('Welcome, venerable', self.name)
        else:
            self.greetingFormal()               

class Wizard(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,'m')
    def greetingFormal(self):
            print('Welcome, Mr', self.name, end=' ')
            print('- you\’re a fine wizard!')
    def spell(self): 
            print('Expelliarmus!')

p1 = Person('Harry',12,'m')
p2 = Person('Jean',22,'f')
p3 = Person('David',61,'m')

p1.greetingInformal()
p2.greetingInformal()
p3.greetingInformal()
p1.greetingFormal()
p2.greetingFormal()
p3.greetingFormal()
p1.greetingAgeBased()
p2.greetingAgeBased() 
p3.greetingAgeBased()

p1 = Wizard('Harry',12,'m')
p1.greetingFormal()
p1.spell()


