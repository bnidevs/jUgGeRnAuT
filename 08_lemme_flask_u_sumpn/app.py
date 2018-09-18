from flask import Flask 

app = Flask(__name__)

@app.route("/0")
def hll_wrld():
	print("about to print __name__...")
	print(__name__)
	return "No hablo queso! 0"

@app.route("/1")
def eo_o():
	print("about to print __name__...")
	print(__name__)
	return "No hablo queso! 1"

@app.route("/2")
def hello_world():
	print("about to print __name__...")
	print(__name__)
	return "No hablo queso! 2"

if __name__ == "__main__":
	app.debug = True
	app.run()