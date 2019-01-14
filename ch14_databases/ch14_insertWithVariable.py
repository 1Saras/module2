# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:07:55 2019

@author: saras
"""

##Task 1 - create table and insert data

#Settings:
import sqlite3 #imports SQLite
import time
import datetime
import random

conn = sqlite3.connect('task1.db') #connects to task1.db database that I am creating now
c = conn.cursor() #connect cursor: links my database to a pointer which finds positions of data in data table

#Table creation:
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)')
#create a table, so we don't have to create a table everytime we run the code, let’s create a function
#about it and only call it when you need to
#inside brackets is SQL
#database name is stuffToBuild  
#column names are: unix, datestamp, keyword, value
#REAL and TEXT are data types

#How to insert data into tables:
def data_entry():
 c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
#put data into the table by using ‘INSERT INTO’ SQL command. Inserting values in the tables columns that were previously created: unix, datestamp, keyword, value
 conn.commit() #prints/shows the info just added, like git commit
# c.close() #if complete the process will need to close the table
# conn.close() #as above

#Call the function to create table:
create_table()
data_entry()



#Task 2 - Inserting data dynamically/add data to table with variables:
def dynamic_data_entry():
 unix = time.time()
 date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
 keyword = 'Python'
 value = random.randrange(0, 10)
 c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword,value) VALUES (?, ?, ?, ?)', (unix, date, keyword,value))
 conn.commit()
 #function to set up variables and insert data into database
 

#Insert multiple rows with a for loop
for i in range(10):
 dynamic_data_entry()
 time.sleep(1) #paces out creation of values so they get different time stamps in the database 
#c.close()
#conn.close() 

#TASK 3- read & select data from a database:

def read_from_db_all():
 c.execute('SELECT * FROM stuffToBuild WHERE value =8 ') #selects everything (*) that has a value of 8 from the database stuffToBuild 
 for row in c.fetchall(): #fetchall() functionis similar to the pull function in Git
     print(row)
#read_from_db_all()
     
def read_from_db2():
 c.execute('SELECT * FROM stuffToBuild WHERE value =2 and unix > 142233222.0 and unix <1547032636.94002 ')
 for row in c.fetchall():
     print(row[0]) #prints unix one values
read_from_db2()

c.close() #closes table 
conn.close() #closes table and database         
     
     
     
     
     
     
     
     
     