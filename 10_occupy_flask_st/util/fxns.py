import random

def csvtodict():
	listofoccs = []
	with open('data/occupations.csv') as f:
		listofoccs = f.read().split("\n") # fill list with rows of csv

	listofoccs.pop(0) #remove header
	listofoccs.pop() #remove total

	psum = 0.0 #use prefix sum for random selection (see below $)

	occdict = {}

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

		occdict[temp[0]] = temp[1]

	return occdict

def regtopsumdict(regdict):
	keys = list(regdict.keys())
	rtrndict = {}
	psum = 0.0
	for k in keys:
		psum += regdict[k]
		rtrndict[k] = psum
	return rtrndict

def randOcc(occdict, keys):
	x = random.random() * 100 #select random float
	b = False
	string = ""
	for k in keys: #loop through %s to find min that is greater than random num
		if x < occdict[k]:
			string = k #found it!
			b = True
			break

	if not b:
		string = "Unemployed" #didn't find it :(((

	return string