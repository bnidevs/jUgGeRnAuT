

import random
from flask import Flask, render_template

app = Flask(__name__)

# following code borrowed from Bill Ni

htmld = {}

def occ():
	l = []
	with open('data/occupations.csv') as f:
		l = f.read().split("\n") # fill list with rows of csv

	l.pop(0) #remove header
	l.pop() #remove total

	d = {} #create dictionary for occupation (key) and percentage (value)
	psum = 0.0 #use prefix sum for random selection (see below $)

	#loop through rows to process/eliminate quotes
	for s in l:
		if s[0:1] == '"': #check for quote
			for i in range(1,len(s)):
				if s[i:i+1] == '"': #look for matching quote
					temp = [s[1:i], s[i+2:]] #remove and split
					break #stop looking for quote
		else:
			temp = s.split(",") #if no quotes
		
		temp[1] = float(temp[1]) #convert string percentage into float
		psum += temp[1] #add percentage to prefix sum

		htmld[temp[0]] = temp[1]
		d[temp[0]] = psum #assign dictionary value to prefix sum

	x = random.random() * 100 #select random float

	keys = list(d.keys()) #get dictionary keys

	b = False
	s = ""
	for k in keys: #loop through %s to find min that is greater than random num
		if x < d[k]:
			s = k #found it!
			b = True
			break

	if not b:
		s = "Unemployed" #didn't find it :(((

	return s

@app.route("/occupations")
def display():
	s = occ() #use this to generate new random occupation each refresh
	return render_template("ting.html", occdict=htmld, randocc=s)

if __name__ == "__main__":
	app.run()




