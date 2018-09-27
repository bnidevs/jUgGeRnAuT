from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display():
	#print(app)
	return render_template("form.html")

@app.route("/auth")
def authen():
	return render_template("return.html", user=request.args["in"], fmeth=request.method)

app.debug = True
app.run()