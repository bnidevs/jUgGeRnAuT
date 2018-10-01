from flask import Flask, render_template, session, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32);

@app.route("/", methods=["GET","POST"])
def display():
	return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login():
	if "bni" in list(session.keys()):
		return render_template("welcome.html",username="bni")
	elif "user" in list(request.form.keys()) and \
		request.form["user"]=="bni" and \
		"pass" in list(request.form.keys()) and \
		request.form["pass"]=="1234":
			return render_template("welcome.html",username="bni")
	return render_template("login.html")

@app.route("/logout", methods=["GET","POST"])
def logout():
	session.pop["bni"];
	return render_template("login.html")

if __name__ == "__main__":
	app.debug = True
	app.run()