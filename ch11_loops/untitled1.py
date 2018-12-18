# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:25:52 2018

@author: saras
"""

x = 33
while x >=1:
        print(x, ': ', end='')
        x = x / 2
print(x)        


def tri_no(n):
    tri_no = 0
    while n > 0:
        tri_no = n + (n - 1)
    print(n)



mark = int(input('Enter student mark '))
if mark >=70:
        print("Top marks that's a first class!")
elif mark >=40:
        print("Well done you passed!")
else:
        print("Sorry that's a fail - you can retake in June")



mark = 1
while mark > 0:
    mark = input('Enter mark: ')
    mark = int(mark)
    print("Student mark is", mark, end='')
    if mark >= 70:
        print(" - first class!")
    elif mark >= 40:
        print(" - that's a pass")
    else:
        print(" - that's a fail")
        
      
  
i = 55
while i > 10:
    print (i)
    i = i * 0.8
    if i==35.2:
        break

    
while True:
    name = input("Please enter name: ")
    if name == "done":
        break
    print ("Hello", name)


