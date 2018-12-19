# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:49:36 2018

@author: saras
"""

##Task 1 & 2#

salary = {} #creates an empty directory

salary['al'] = 20000
salary['Sarika'] = 800 000
salary['Jenny'] = 700000
print(salary)


##Task 2 - create own dictionary
tel = {}
tel = {'alf':111, 'bobby':222, 'calvin':333}
print(tel)

#adding new entries
tel['Martiena'] = 145
tel['Mag'] = 281
tel['Mag'] = '281'
print(tel)

#updating existing values
tel['Mag'] = 2812
print(tel)

tel['Martiena'] = 821
print(tel)

#deleting a key value pair
del tel['bobby']
print(tel)


##Task 3 - accessing the dictionary
print(tel['Mag'])


##Task 4 - getting keys and values from a dictionary
print(tel.keys())
print(tel.values())


#cast to standardised list, looks the same when printed but can now do operations to it#
list_of_tel_keys=list(tel.keys())

list(tel.keys())[0]

list_of_tel_values=list(tel.values())
list(tel.keys())[0]


##Task 6 - how to avoid key errors

k = 'Sam'

if k in tel:
    print(k, ':', tel[k])
    
else:
    print(k, 'not found!')

#Mag is in the dictionary so her data will be printed#
k = 'Mag'

if k in tel:
    print(k, ':', tel[k])
    
else:
    print(k, 'not found!')


##Task 7 
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k]) 
print(labels)
print(counts)   
counts['g']=8
counts['f']=10
counts['o']=20
print(counts)    

#Another example#
tel = {}
tel = {'alf':('March', 111), 'bobby':('June', 222), 'calvin':('Sept', 333), 'Martiena':('May', 821), 'Mag':('Nov', 281)}
print(tel)

labels = list(tel.keys())

labels.sort(key=lambda k:tel[k])
print(labels)

tel_keys = list(tel.keys())

tel_keys.sort(key=lambda k:tel[k][1])
print (tel_keys)

print(sorted(tel.items(), key=lambda kv:kv[1]))

print(sorted(tel.items(), key=lambda kv:kv[0]))



metals = {'iron':(7.8, 12.5, 498), 'gold':(19.3, 32.1, 230), 'zinc':(7.13, 84.8, 879), 'lead':(11.4, 98.1, 384)}
print(metals)

#turns the tuples into lists#
metals_keys = list(metals.keys())
#
#sorts by share price accending#
print(sorted(metals.items(), key=lambda kv:kv[1][1]))

##sorts by share price in reverse order#
#print(sorted(metals.items(), key=lambda kv:kv[1][1],reverse=True))
#
##sorts by share price in reverse order but only showing the keys#
#metals_keys.sort(key=lambda k:metals[k][1],reverse=True)
#print(metals_keys)

#sorting by experiment ascending#
#print(sorted(metals.items(), key=lambda kv:kv[1][2]))
#sorted(densities, reverse=True,key=lambda m:densities[m] [1] [0])
sorted(metals.items(),key=lambda kv:kv[1][1],reverse=True)
sorted(metals.items(),key=lambda kv:kv[1][1],reverse=True)[2]



 