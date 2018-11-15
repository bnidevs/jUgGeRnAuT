from urllib import request, parse, error
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display():
	url = "https://ipapi.co/json/"
	f = request.urlopen(url).read()
	d = json.loads(f)
	lon = d["longitude"]
	lat = d["latitude"]

	url = "https://api.nasa.gov/planetary/earth/imagery/?"
	data = {}
	data["lon"] = str(lon)
	data["lat"] = str(lat)
	data["dim"] = 0.1
	data["cloud_score"] = "True"

	try: data["api_key"] = open("key.txt").read()
	except: data["api_key"] = "DEMO_KEY"

	url += parse.urlencode(data)

	f = request.urlopen(url).read()
	d = json.loads(f)
	return render_template("main.html", piclink=d["url"])

app.debug = True
app.run()