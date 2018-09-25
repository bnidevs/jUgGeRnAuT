#cOpS aNd rObBeRs - Robin Han, Bill Ni
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-21

import random
from flask import Flask, render_template
from util import fxns

app = Flask(__name__)

htmldict = fxns.csvtodict() #create dictionary for occupation (key) and percentage (value)
psumdict = fxns.regtopsumdict(htmldict)
keys = list(psumdict.keys())

@app.route("/")
def dis1():
	return '<a href="./occupations"> go to occupations </a>'

@app.route("/occupations")
def dis2():
	s = fxns.randOcc(psumdict, keys) #use this to generate new random occupation each refresh
	return render_template("ting.html", occdict=htmldict, randocc=s)

if __name__ == "__main__":
	app.run()