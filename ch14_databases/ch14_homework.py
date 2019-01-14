# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:25:22 2019

@author: saras
"""

import sqlite3
import time
import random

#connect database:
conn = sqlite3.connect('homework.db')
#connect cursor:
c = conn.cursor() 

#create a table, so e don't have to create a table everytime we run the code, let’s create a function
#about it and only call it when you need to:
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook2(First_Name TEXT , Last_Names TEXT, Address_Line TEXT, City TEXT)')
    
#put data into the table by using ‘INSERT INTO’ SQL command
def data_entry():
 c.execute("INSERT INTO phonebook2 VALUES('Sara', 'Sar', 'St Pauls', 'London')")
 conn.commit()
 c.close()
 conn.close()

#Call the function to create table:
#create_table()
#data_entry()
# 
def dynamic_data_entry():
 First_Name = 'Sam'
 Last_Names = 'Smith'
 Address_Line = 'Pudding Lane'
 City = 'Manchester'
 c.execute('INSERT INTO phonebook2(First_Name, Last_Names, Address_Line, City) VALUES (?, ?, ?, ?)', (First_Name, Last_Names, Address_Line, City))
 conn.commit()


for i in range(10):
 dynamic_data_entry()

c.close()
conn.close() 
 