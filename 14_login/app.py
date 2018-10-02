# Team Hakuna Matata - Aleksandra Koroza, Bill Ni
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-01

from flask import Flask,render_template,session,request,redirect,url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32);

#hardcoded credentials
usnm= "bni"
psswd= "1234"

@app.before_request
def make_session_permanent():
        session.permanent = True

@app.route("/", methods=["GET","POST"])
def display():
        if usnm in list(session.keys()):
	        return render_template("welcome.html",username=usnm)
        return render_template("login.html")


@app.route("/login", methods=["GET","POST"])
def login():
        uBool= "user" in list(request.form.keys()) and request.form["user"]== usnm
        pBool= "pass" in list(request.form.keys()) and request.form["pass"]== psswd
        
	if uBool and pBool:
        return render_template("welcome.html",username=usnm)
	elif not uBool or not pBool:
        return render_template("error.html",userBool= str(uBool),passBool= str(pBool))
	else:
        return render_template("login.html")
                
@app.route("/logout", methods=["GET","POST"])
def logout():
    session.pop[usnm]
    return render_template("login.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
