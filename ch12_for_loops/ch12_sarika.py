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
#    
#for val in values:
#    print('---> '+str(val+50)) 
#    
#for val in values:
#    print('---> '+str(val), '---> '+str(val+50) )
#    
#for val in values:
#    print('---> '+str(val), '---> '+str(val-50) )
#    
#for val in values:
#    print('---> '+str(val), '---> '+str(val*4.5) )
#    
#for val in values:
#    print('---> '+str(val), '---> '+str(val/2.1) )
#
#for val in values:
#    print('---> '+str(val), '---> '+str(val%2.1) )
#
#
#
###Task 3#
#values = ['plane', 125, 'train', 'car', 26, 'tram', 'bike']
#for item in values:
#    print('/-/', item)



##Task 4#
#for char in "Yes":
#    print(char)    
#    
#for char in "It's Thursday today":
#    print(char) 

#for char in "It's Thursday today".split():
#    print(char)
#    
#for char in "It's Thursday today".split('o'):
#    print(char)
#        
#for char in "It's-Thursday-today".split('-'):
#    print(char)



###Task 5-tuple#
#restaurant = ("Indian", "Mexican", "Italian", "Chinese", "French")
#for item in restaurant:
#    print(item)
#    
#
#
###Task 6-dictionary
#
#salaries = {'al':20000, 'bo':50000, 'ced':1500}
#employees = list(salaries.keys())
#print(employees)
#
#employees.sort(key=lambda s:salaries[s])
#print(employees)
#
#
#
##Task 7 & Task 8
#
#densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
#metals = list(densities.keys())
#print(metals)
#
#metals.sort(reverse=True,key=lambda m:densities[m])
#print (metals)
#
#for metal in metals:
#    print('{0:>8} = {1:5.1f}'.format(metal,densities[metal]))
#

##Another example
densities = {'iron':(7.8, 12.5, 498), 'gold':(19.3, 32.1, 230), 'zinc':(7.13, 84.8, 879), 'lead':(11.4, 98.1, 384)}
metals = list(densities.keys())
    
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
#    if densities[metal][0]>15:
#        print("Density above 15:", metal,densities[metal][0])
#    else:
#        print("Density less than 15:", metal,densities[metal][0])
#
#
#        
###Task 9 & 10#

#valuesList = [3, 12, 9]
#total = 0
#for value in valuesList:
#    print('before adding',value, 'total is', total)
#    total = value + total
#    print('after adding',value, 'total is', total)

#values = [3, 12, 9]
#total = 0
#for val in values:
#    total += val
#print('TOTAL:' + str(total)) 
##prints TOTAL: 24
#
#def sumValues(l):
#    sumV = 0
#    for val in l:
#        sumV +=val
#    return sumV
#print (sumValues(values))
##prints 24
#
#for i in range(len(values)):
#    values[i] = values[i] * 2
#print(values) 
##prints [6, 24, 18]
#
#print(len(values))
##prints 3
#
#print (list(range(6)))
##prints [0, 1, 2, 3, 4, 5]

##another example


values = [3, 12, 9, 2, 3, 4, 5, 6]
#
#for v in values:    
#    print(values) 
#    #prints [3, 12, 9, 2, 3, 4, 5, 6] eight times as there are 8 values
    
for index in range(len(values)):
    print(index) #prints 
#    
#for index in range(len(values)):
#    print(values[index]) #prints 3,12,9
#    
#for index in range(0,len(values),3):
#    print(values[index]) 
#
#values = [3, 12, 9]
#for index in range(len(values)):
#    values[index] = values[index] * 2
#    print(values)
#    
#for index in range(3,10,2):
#    print(index)
#    print(list(range(3)))
#
#nums = [1, 5, 30, 200, 101, 100, 22]
#for n in nums:
#    if n >100:
#        print('break:', n)
#        break
#
#nums = [1, 5, 30, 200, 101, 100, 22]
#for index in range (len(nums)):
##    print('loop index',index,'with value',num[index])
#    if nums[index] > 100:
#        print ('need to break:', nums[index], 'with index',index)
#    else:
#        print('oh you forgot to break the loop!',nums[index],'with index',index)
#        
#        
#outer_vals = [1, 2, 3]
#inner_vals = ['A', 'B', 'C']
#d = {}
#for oval in outer_vals:
##    print(oval)
#    for ival in inner_vals:
#        print(ival)
#        d[oval] = ival
#        print(d)
# 
#
#outer_vals = [1, 2, 3]
#inner_vals = ['A', 'B', 'C']
#d = {}
#for oval in outer_vals:
##    print(oval)
#    for ival in ['A', 'B', 'C']:
#        d[oval] = ival
#        print(d)
#        
#outer_vals = [1, 2, 3]
#inner_vals = ['A', 'B', 'C']
#d = {}    
#for outer_val in [1, 2, 3]:
#    for inner_val in ['A', 'B', 'C']:
#        d[outer_val] = inner_val
#        print(outer_val,inner_val)
# 

#
#
# 
#Christmas_Wish = {'books': (5), 'holidays': (1), 'chocolates': (25)}
#loopRound = 0
#for gift, item in Christmas_Wish.items():
#    print('open box', loopRound, 'the gift is', gift)
#    print('the item is', item)
#    if item >=4:
#        print ('Yay! I am so happy to be getting', item, gift, '.')
#    else:
#         print ('Oh no please get me more', 'of', gift, '.')
#         
#    loopRound +-1
#
#Christmas_List = {'book': (5, 10.99), 'holidays': (3, 5000), 'chocolates': (25, 30)}













       
        




