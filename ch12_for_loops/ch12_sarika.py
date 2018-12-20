# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:06 2018

@author: saras
"""


##Task 1#

#my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
#for item in my_shopping_cart:
#    print(item)
 


##Task 2#
   
#values = [875, 23, 451]
#for val in values:
#    print('---> '+str(val))
#    print('---> '+str(val+50))   
#    print('---> '+str(val), '---> '+str(val+50) )
   


##Task 3#
#values = ['this', 55, 'that']
#for item in values:
#    print('***', item)



##Task 4#
#for char in "Yes":
#    print(char)    
#    
#for char in "It's Thursday today":
#    print(char) 
#
#for char in "It's Thursday today":
#    print(char)

#for char in "It's Thursday today".split():
#    print(char)
#    
#for char in "It's Thursday today".split('o'):
#    print(char)
        
#for char in "It's-Thursday-today".split('-'):
#    print(char)



##Task 5#
#restaurant = ("Indian", "Mexican", "Italian", "Chinese")
#for item in restaurant:
#    print(item)
#    
    

#densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
#metals = list(densities.keys())
#print(metals)


##Task 8#
#densities = {'iron':(7.8, 12.5, 498), 'gold':(19.3, 32.1, 230), 'zinc':(7.13, 84.8, 879), 'lead':(11.4, 98.1, 384)}
#metals = list(densities.keys())
    
#for metal in metals:
#    print(metal) 
#      
#for metal in metals:
#    print(densities[metal])
#
#for metal in metals:
#    print(metal, densities[metal])
#    
#for metal in metals:
#    print(metal, densities[metal][1]) 
#
#for k, v in sorted(densities.items(), key = lambda kv:kv[1][1]):
#    print()
#
#for k, v in sorted(densities.items(), key = lambda kv:kv[1][1], reverse=True):  
#    print(k,v[1])
#    
#for metal in metals:
#        print(metal, densities [metal][1])
              
#for metal in metals:
#    if densities[metal][0]>8:
#        print('{0:>8} = {1:5.1f}'.format(metal,densities[metal][0]))
#
#for metal in metals:
#    if densities[metal][0]>15:
#        print(metal,densities[metal][0])

        
##Task 9#
#valuesList = [3, 12, 9]
#total = 0
#for value in valuesList:
#    print('before adding',value, 'total is', total)
#    total = value + total
#    print('after adding',value, 'total is', total)

 
Christmas_Wish = {'books': (5), 'holidays': (3), 'chocolates': (25)}
loopRound = 0
for gift, item in Christmas_Wish.items():
    print('open box', loopRound, 'the gift is', gift)
    print('the item is', item)
    if item >=4:
        print ('Yay! I am so happy to be getting', item, gift, '.')
    else:
         print ('Oh no please get me more', 'of', gift, '.')
         
    loopRound +-1

#Christmas_List = {'book': (5, 10.99), 'holidays': (3, 5000), 'chocolates': (25, 30)}















