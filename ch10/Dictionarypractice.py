# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:49:36 2018

@author: saras
"""
###Line 8 is an example of a dictionary#
#{'bo': 50000, 'al': 20000, 7: ('Joke', 'Chen', 'Bond')}
#
##creates an empty dictionary#
#salary = {}
#salary 
#{}


#salary['al'] = 20000
#salary['Sarika'] = 20000000
#salary['Jenny'] = 110000
#print(salary)
#
#salary['al']+=2000
#print(salary)
#
#
tel = {}
#tel = {'alf':111, 'bobby':222, 'calvin':333}
#
#tel['Martiena'] = 145
#tel['Mag'] = 281
#tel['Mag'] = '281'
#print(tel)
#
#tel['Mag'] = 2812
#print(tel)
#
#tel['Martiena'] = 821
#print(tel)
#
#del tel['bobby']
#print(tel)
#
##get keys and values#
#print(tel.keys())
#print(tel.values())
#
##cast to standardised list#, looks the same when printed but can now do operations to it
#list(tel.keys())[0]
#print(tel.keys())
#
##Avoiding key errors - the below avoids error message#
#k = 'Sam'
#
#if k in tel:
#    print(k, ':', tel[k])
#    
#else:
#    print(k, 'not found!')
#
##Mag is in the dictionary so her data will be printed#
#k = 'Mag'
#
#if k in tel:
#    print(k, ':', tel[k])
#    
#else:
#    print(k, 'not found!')

##
#counts = {'a': 3, 'c': 1, 'b': 5}
#labels = list(counts.keys())
#labels.sort(key=lambda k:counts[k])
#
#print(labels)
#print(counts)
#
#counts['g']=8
#counts['f']=10
#counts['o']=20
#
#print(counts)

#I've started again and am adding 2 values to tel list#
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
