# Team Hakuna Matata - Aleksandra Koroza, Bill Ni
# SoftDev1 pd8
# K15 -- Oh yes, perhaps I do…  
# 2018-10-02

from flask import Flask,render_template,session,request,redirect,url_for,flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32);

#hardcoded credentials
usnm = "bni"
psswd = "1234"

@app.route("/", methods=["GET","POST"])
def display():
    if 'username' in session:
        return render_template("welcome.html",username=usnm)
    return render_template("login.html")


@app.route("/login", methods=["GET","POST"])
def login():
    uBool = "user" in list(request.form.keys()) and request.form["user"] == usnm
    pBool = "pass" in list(request.form.keys()) and request.form["pass"] == psswd

    if uBool and pBool:
        session['username']=usnm
        return render_template("welcome.html",username=usnm)
    elif not uBool or not pBool:
        flash("Oops something went wrong")
        flash("Username correct?: " + str(uBool))
        flash("Password correct?: " + str(pBool))
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET","POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for('display'))

if __name__ == "__main__":
    app.debug = True
    app.run()
