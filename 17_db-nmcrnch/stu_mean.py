import sqlite3

def resetc1():
	c1.execute("SELECT * FROM courses")

def resetc2():
	c2.execute("SELECT * FROM peeps")

dbcourses = sqlite3.connect("discobandit.db") # courses
c1 = dbcourses.cursor()
c1.execute("SELECT * FROM courses")

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

print(gradeLookup(1, c1))

c1.execute("SELECT * FROM courses")

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

print(compAvg(1, c1))

dbstudents = sqlite3.connect("derivativeballoon.db")
c2 = dbstudents.cursor()
c2.execute("SELECT * FROM peeps")
c1.execute("SELECT * FROM courses")

def displayStuInfo(stuid, cursor1, cursor2):
	rtrnStr = ""
	for row in cursor1:
		if stuid == row[2]:
			rtrnStr += row[0] + " " + str(stuid)
	if rtrnStr == "":
		rtrnStr = "STUDENT NOT FOUND"
	else:
		rtrnStr += str(compAvg(stuid, cursor1))
	return rtrnStr




