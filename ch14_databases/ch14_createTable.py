# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:07:55 2019

@author: saras
"""

import sqlite3
#connect database:
conn = sqlite3.connect('task1.db')
#connect cursor:
c = conn.cursor() 

#create a table, so e don't have to create a table everytime we run the code, let’s create a function
#about it and only call it when you need to:
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)')
    
#put data into the table by using ‘INSERT INTO’ SQL command
def data_entry():
 c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
 conn.commit()
 c.close()
 conn.close()

#Call the function to create table:
create_table()
data_entry()

