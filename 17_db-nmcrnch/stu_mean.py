#DiscoAtThePanic: Robin Han, Bill Ni
#SoftDev1 pd8
#K17 -- Average
#2018-10-05

import sqlite3

# resets cursors to read from the csv from the beginning
def resetc1():
	c1.execute("SELECT * FROM courses")

def resetc2():
	c2.execute("SELECT * FROM peeps")

dbcourses = sqlite3.connect("discobandit.db") # courses
c1 = dbcourses.cursor()
dbstudents = sqlite3.connect("derivativeballoon.db") # students
c2 = dbstudents.cursor()
resetc1()
dbtable = sqlite3.connect("dinoball.db") #new table
c3 = dbtable.cursor()

print("gradeLookup test:\n")

# Looks up the grade of each class a given student is taking by ID.
def gradeLookup(stuid, cursor):
	rtrnStr = ""
	for row in cursor:
		if stuid == row[2]:
			rtrnStr += row[0] + " " + str(row[1]) + "\n"
	if rtrnStr != "":
		rtrnStr = rtrnStr[:-1]
	else:
		rtrnStr = "STUDENT NOT FOUND"
	return rtrnStr

# testing gradeLookup
print(gradeLookup(1, c1))
print("\n\n\n")
#----------------------------

resetc1()
print("compAvg test:\n")
#Computes the overall average of the classes a student is taking. Also by ID
def compAvg(stuid, cursor):
	sumgrades = 0
	numgrades = 0
	for row in cursor:
		if stuid == row[2]:
			sumgrades += row[1]
			numgrades += 1
	if numgrades == 0:
		return "STUDENT NOT FOUND"
	return (sumgrades + 0.0) / numgrades
#testing compAvg
print(compAvg(1, c1))
print("\n\n\n")
#---------------------------

resetc2()
resetc1()
print("displayStuInfo test:")

#Displays students name, id, and overall average.
def displayStuInfo(stuid, cursor1, cursor2):
	rtrnStr = ""
	for row in cursor2:
		if stuid == row[2]:
			rtrnStr += row[0] + " " + str(stuid) + " "

	if rtrnStr == "":
		rtrnStr = "STUDENT NOT FOUND"
	else:
		rtrnStr += str(compAvg(stuid, cursor1))
	return rtrnStr

# testing displayStuInfo
print(displayStuInfo(3, c1, c2))
print("\n\n\n")
#-----------------------------


#Creates a peeps_avg table to store a student's ID and average
def createTable(cursor):
        cursor.execute("CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, average INTEGER)")

#Adds and new course, id, and mark to the existing tables list. 
def add_course(code, new_id, mark,cursor):
        cursor.execute("INSERT INTO courses (code, id, mark) VALUES('" + str(code) + "'," + str(new_id) + "," + str(mark) + ")")

#Testing add_course
print("add_course test: \n")
add_course('engrish', 5, 98,c1)
resetc1()
c1.execute("SELECT * FROM courses")
print(c1.fetchall())
                