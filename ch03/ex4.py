# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:54:12 2018

@author: saras
"""
#Lines 8 to 15 are giving variables and their values so that they can be used in calculations and printed#
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#prints the number in line 8#
print ("There are", cars, "cars available.")

#prints the number in line 10#
print ("There are only", drivers, "drivers available.")

#calculates the equation in line 12#
print ("There will be", cars_not_driven, "empty cars today.")

#calculates the equation in line 14#
print ("We can transport", carpool_capacity, "people today.")

#prints the number in line 11#
print ("We have", passengers, "to carpool today.")

#calculates the equation in line 15#
print ("We need to put about", average_passengers_per_car, "in each car.")