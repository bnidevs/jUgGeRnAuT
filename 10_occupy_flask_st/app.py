#cOpS aNd rObBeRs - Robin Han, Bill Ni
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-21

import random
from flask import Flask, render_template

app = Flask(__name__)

# following code borrowed from Bill Ni

htmld = {}
occdict = {} #create dictionary for occupation (key) and percentage (value)

def occ():
	listofoccs = []
	with open('data/occupations.csv') as f:
		listofoccs = f.read().split("\n") # fill list with rows of csv

	listofoccs.pop(0) #remove header
	listofoccs.pop() #remove total

	psum = 0.0 #use prefix sum for random selection (see below $)

	#loop through rows to process/eliminate quotes
	for occs in listofoccs:
		if occs[0:1] == '"': #check for quote
			for i in range(1,len(occs)):
				if occs[i:i+1] == '"': #look for matching quote
					temp = [occs[1:i], occs[i+2:]] #remove and split
					break #stop looking for quote
		else:
			temp = occs.split(",") #if no quotes
		
		temp[1] = float(temp[1]) #convert string percentage into float
		psum += temp[1] #add percentage to prefix sum

		htmld[temp[0]] = temp[1]
		occdict[temp[0]] = psum #assign dictionary value to prefix sum

	x = random.random() * 100 #select random float

	return list(d.keys()) #get dictionary keys

	
def randOcc(keys):
	b = False
	string = ""
	for k in keys: #loop through %s to find min that is greater than random num
		if x < d[k]:
			string = k #found it!
			b = True
			break

	if not b:
		string = "Unemployed" #didn't find it :(((

	return string

keys = occ()

@app.route("/occupations")
def display():
	s = randOcc(keys) #use this to generate new random occupation each refresh
	return render_template("ting.html", occdict=htmld, randocc=s)

if __name__ == "__main__":
	app.run()




