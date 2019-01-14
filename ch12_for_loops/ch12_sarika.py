# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:06 2018

@author: saras
"""



##Task 1 - loop through a list using a for loop

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart: #'item' activates the loop for the items
    print(item)
#prints:
#cake
#plates
#plastic forks
#juice
#cups

#Recap the list data type  
x = ['aa', 'bb', 'cc']
x[1] = 33 #replacing bb with 33
print(x)
#prints:
#['aa', 33, 'cc']

x.append('dd') #adding 'dd' to the end of the list
print(x)
#prints:
#['aa', 33, 'cc', 'dd']
  


##Task 2 - update list values
   
values = [875, 23, 451]


for val in values: #val can be any word
    print('---> '+str(val))  
#prints:
#---> 875
#---> 23
#---> 451

#the loop goes into the list and select first value and prints it after --->, then gets to the second and prints until the list is finished 

   
for val in values:
    print('---> '+str(val+50)) #adds 50 to each value
#prints:   
#---> 925
#---> 73
#---> 501    
        
    
for val in values:
    print('---> '+str(val), '---> '+str(val+50) )
# prints:
#---> 875 ---> 925
#---> 23 ---> 73
#---> 451 ---> 501

    
for val in values:
    print('---> '+str(val), '---> '+str(val-50) )
# prints:
#---> 875 ---> 825
#---> 23 ---> -27
#---> 451 ---> 401
    
       
for val in values:
    print('---> '+str(val), '---> '+str(val*4.5) )
#prints:
#---> 875 ---> 3937.5
#---> 23 ---> 103.5
#---> 451 ---> 2029.5
    
       
for val in values:
    print('---> '+str(val), '---> '+str(val/2.1) )
#prints:
#---> 875 ---> 416.66666666666663
#---> 23 ---> 10.952380952380953
#---> 451 ---> 214.76190476190476
    
       
    
##Task 3 -create own list
    
values = ['plane', 125, 'train', 'automobile', 26,]
for item in values:
    print('/-/', item)
#prints:
#/-/ plane
#/-/ 125
#/-/ train
#/-/ automobile
#/-/ 26



##Task 4-loop through a string type

for char in "Yes":
    print(char)    
#prints:
#Y
#e
#s
   
    
for char in "It's Thursday".split():
    print(char)
#prints:
#It's
#Thursday


for char in "It's Thursday today".split('o'):
    print(char)
#prints:
#It's Thursday t
#day    
    
    
for char in "It's-Thursday-today".split('-'):
    print(char)
#prints:
#It's Thursday t
#day



##Task 5-loop through a tuple
    
restaurant = ("Indian", "Mexican", "Chinese")
for item in restaurant:
    print(item)
#prints:
#Indian
#Mexican
#Chinese    



##Task 6&7-looping through a sorted dictionary
  
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print(metals)
#prints:
# ['iron', 'gold', 'zinc', 'lead']    
 
    
metals.sort(reverse=True,key=lambda m:densities[m]) #to sort by value need to use lambda function. The m is for the key. can you any word in place of m
print (metals)
#prints:
#['gold', 'lead', 'iron', 'zinc'] #reverse value i.e decending order (highest to lowest)


for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal,densities[metal]))
#prints:
#    gold =  19.3
#    lead =  11.4
#    iron =   7.8
#    zinc =   7.1


##Task 8-Combine counting loop and conditionals to filter out values 

Christmas_Wish = {'books': (5), 'holidays': (1), 'chocolates': (12)}

for gift, item in Christmas_Wish.items():
    print('The gift is', gift)
    print('There are', item, gift)
    if item >=5:
        print ('Yay- thanks so much! I am so happy to be getting', item, gift, '\n')
    else:
         print ('Oh no please get me more', gift, '\n')
             
#prints:
#The gift is books
#There are 5 books
#Yay- thanks so much! I am so happy to be getting 5 books 
#
#The gift is holidays
#There are 1 holidays
#Oh no please get me more holidays 
#
#The gift is chocolates
#There are 12 chocolates
#Yay- thanks so much! I am so happy to be getting 12 chocolates


##Task 9- design a sum fuction

values = [3, 12, 9]
total = 0
for val in values:
    total += val #same as total=total+val
print('TOTAL:' + str(total)) 
#prints TOTAL:24
                    
        
def sumValues(l):
    sumV = 0
    for val in l:
        sumV +=val
    return sumV
print (sumValues(values))
#prints 24



valuesList = [8, 7, 89]
total = 0

for value in valuesList:
    print('before adding',value, 'total is', total)
    total = value + total
    print('after adding',value, 'total is', total)
    print('Total:' + str(total))
#prints:
#before adding 8 total is 0
#after adding 8 total is 8
#Total:8
#before adding 7 total is 8
#after adding 7 total is 15
#Total:15
#before adding 89 total is 15
#after adding 89 total is 104
#Total:104         
         

##Task 10 - using a loop with index values
values = [12,3,22]
for i in range(len(values)):
    values[i] = values[i] * 2
    print(values)     
#prints:
#[24, 3, 22]
#[24, 6, 22]
#[24, 6, 44]
    
    
##task 11: using a loop with the range function   
    
for i in range(3):
    print(i) 
#prints 
#0
#1
#2    
    
for index in range(len(values)):
    print(index) 
#prints 
#0
#1
#2  
 
    
#another example

values = [3, 12, 9]

for v in values:    
    print(values) 
#prints: 
#[3, 12, 9] 
#[3, 12, 9] 
#[3, 12, 9] 
#as there are three values
    
       
    
##Task 12
    
nums = [1, 19, 25, 101, 100, 22]
for item in nums:
    if item >100:
        print('stops at:', item)
        break
#prints:
#stops at: 101        
    
nums = [1, 19, 25, 101, 100, 22]
for index in range (len(nums)):
#    print('loop index',index,'with value',num[index])
    if nums[index] > 100:
        print ('need to break:', nums[index], 'with index',index)
    else:
        print('oh you forgot to break the loop!',nums[index],'with index',index)

#prints:
#oh you forgot to break the loop! 1 with index 0
#oh you forgot to break the loop! 19 with index 1
#oh you forgot to break the loop! 25 with index 2
#need to break: 101 with index 3
#oh you forgot to break the loop! 100 with index 4
#oh you forgot to break the loop! 22 with index 5



##Task 13 - nested loops
    
outer_vals = [1, 2, 3]
inner_vals = ['A', 'B', 'C']
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)

#prints:
#1 A
#1 B
#1 C
#2 A
#2 B
#2 C
#3 A
#3 B
#3 C



##Task 14 - multiplication table with a for loop
  
for i in range(1,7):
   for j in range(1,11):
      print('{0:>3}'.format(i * j), end='')
   print('\n')

#prints:
#1  2  3  4  5  6  7  8  9 10
#
#2  4  6  8 10 12 14 16 18 20
#
#3  6  9 12 15 18 21 24 27 30
#
#4  8 12 16 20 24 28 32 36 40
#
#5 10 15 20 25 30 35 40 45 50

#6 12 18 24 30 36 42 48 54 60

#Loop takes the first loop i (from 1 to 7) takes the first number (1) 
#Then goes to the second loop (from 1 to 11) takes the first number (again 1) so does 1*1
#Then 1 * 2, 1 * 3 until 1*10. 
#Then will go to 2 and ill do: 2*1, 2*2 until 2*10. 
#Then 3*1 etc until all are finished up until the final one 6*10 which is 60
   
for i in range(1,11):
   for j in range(1,11):
      print('{0:>3}'.format(i * j), end='')
   print('\n')   
#until 10*10
   
