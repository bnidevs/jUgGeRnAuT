import json
from urllib import request, parse, error
from random import randint

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display():
	# nasa

	url = "https://api.nasa.gov/planetary/earth/imagery/?"
	data = {}
	data["lon"] = "100.75"
	data["lat"] = "1.5"
	data["date"] = "2014-02-01"
	data["cloud_score"] = "True"
	
	try: data["api_key"] = open("key.txt").read()
	except: data["api_key"] = "DEMO_KEY"

	url += parse.urlencode(data)

	f = request.urlopen(url).read()
	d = json.loads(f)

	pL = d["url"]

	# news

	url = "https://newsapi.org/v2/top-headlines?"
	data = {}
	data["country"] = "us"

	try: data["apiKey"] = open("newskey.txt").read()
	except: data["apiKey"] = "API_KEY"

	url += parse.urlencode(data)

	f = request.urlopen(url).read()
	d = json.loads(f)

	r = randint(0, d["totalResults"] - 1)
	nL = d["articles"][r]["url"]
	nT = d["articles"][r]["title"]

	# trivia

	url = "https://opentdb.com/api.php?"
	data = {}
	data["amount"] = "1"
	data["category"] = str(randint(9, 32))
	data["difficulty"] = "medium"
	data["type"] = "multiple"

	url += parse.urlencode(data)

	f = request.urlopen(url).read()
	d = json.loads(f)

	q = d["results"][0]["question"]
	a = d["results"][0]["correct_answer"]

	# poem

	url = "https://www.poemist.com/api/v1/randompoems"

	f = request.urlopen(url).read()
	d = json.loads(f)[0]

	pT = d["title"]
	pC = d["content"]
	poetL = d["poet"]["url"]
	poetN = d["poet"]["name"]

	return render_template("main.html", piclink=pL, newslink=nL, title=nT, question=q, ans=a, poemtitle=pT, poem=pC, poetname=poetN, poetlink=poetL)

app.run()