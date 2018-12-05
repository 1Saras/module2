# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:44:56 2018

@author: saras
"""
#ch 03#
#ch3_Sarika#


#from lines 80 and 81#
def hello_world_4args(a, b, c, d):
    print ("{} {} {} {}".format(a, b, c, d))
    



#from lines 127 to 131#
def convert_temperature(): 
    centigrade = int(input("What temperature in centigrade do you want to convert to fahrenheit and kelvin?"))
    fahrenheit = (centigrade * 9.0) / 5.0 + 32
    kelvin = centigrade + 273.15
    return (centigrade, fahrenheit, kelvin)
    







    
    
    
    
    