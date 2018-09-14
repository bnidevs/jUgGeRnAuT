#aNtMan aNd tHe wAsP - Johnson Li, Bill Ni
#SoftDev1 pd8
#K06 -- Stl/O: Divine your Destiny!
#2018-09-13

import random

l = []
with open('occupations.csv') as f:
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

	d[temp[0]] = psum #assign dictionary value to prefix sum

x = random.random() * 100 #select random float

keys = list(d.keys()) #get dictionary keys

b = False
for k in keys: #loop through %s to find min that is greater than random num
	if x < d[k]:
		print(k) #found it!
		b = True
		break

if not b:
	print("Unemployed") #didn't find it :(((

# $ see above for reference
#
# the way our prefix sum algo works is our percentages are no longer
# separate but cumulative, so our randomization is made easier
# for example: let's use a smaller case
# if there are 3 things we can do, and each has a 33.3% chance of
# happening, we can add them cumulatively to get
# 33.3, 66.7 and 100 and we just pick a random number in between 0
# and 100, and check the interval it's in
#
# it doesn't matter whether the numbers are in order or not 
# because each of the percentages given are equal to the range of
# numbers that it receives




