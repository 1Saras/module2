# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:04 2018

@author: saras
"""


"""
Creating an empty function
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        if checkBalance(balance):
            print ('Your balance is {}'.format(balance))
            return ask_transaction(balance)
        else:
            return ('Your balance is not sufficient: {}'.format(balance))
    else:
        return 'Wrong password'


def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
    
def ask_transaction(balance):
    print ('Which transaction would you like you carry out? Please input the number 1 or 2')
    print ('1 Check balance')
    print ('2 Purchase data bundle')
    ask = input()
    if ask == '1':
        print ('Your balance is {}'.format(balance)) 
    elif ask == '2':
        print ('What is your phone number?')
        phone1 = input(number1)
        print ('Please re-enter your phone number to validate')
        phone2 = input(number2)
    else:
        print ('You must input the number 1 or 2')

def phone1(number1):
    
def phone2(number2):      
     
#print ('How much credit would you like to purchase? Your input must be a multiple of 5')
#return multiple_of_five()


#def check_against_balance(amount):
#     if balance    
    
#def multiple_of_five():
#    if mutiple ==    

    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    