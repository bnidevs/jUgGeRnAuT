from flask import Flask, render_template
from urllib import request, parse, error
import json

app = Flask(__name__)

@app.route("/")
def display():
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
	return render_template("main.html", piclink=d["url"])

app.debug = True
app.run()