#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

with open("courses.csv") as csvfile:
	read = csv.DictReader(csvfile)
	for row in read:
		c.execute("INSERT INTO courses (code, mark, id) VALUES('" + row["code"] + "','" + row["mark"] + "','" + row["id"] + "')" )
		
c.execute("SELECT * FROM courses")
print( c.fetchall())
db.commit() #save changes
db.close()  #close database
