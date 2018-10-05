#Team Pepe2.0 -- Jack Lu, Bill Ni
#SoftDev1 pd8
#K16 - No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

# ********************************FIRST DB*********************************

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

with open("courses.csv") as csvfile:
	read = csv.DictReader(csvfile)
	for row in read:
		c.execute("INSERT INTO courses (code, mark, id) VALUES('" + row["code"] + "'," + row["mark"] + "," + row["id"] + ")" )
		
# c.execute("SELECT * FROM courses")
# print( c.fetchall())
db.commit() #save changes
db.close()  #close database

# ********************************SECOND DB********************************

DB_FILE="derivativeballoon.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)")

with open("peeps.csv") as csvfile:
	read = csv.DictReader(csvfile)
	for row in read:
		c.execute("INSERT INTO peeps (name, age, id) VALUES('" + row["name"] + "'," + row["age"] + "," + row["id"] + " )" )
		
# c.execute("SELECT * FROM peeps")
# print( c.fetchall())
db.commit() #save changes
db.close()  #close database