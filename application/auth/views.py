from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, BreederForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/kirjautuminen.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/kirjautuminen.html", form = form,
                               error = "Salasana tai käyttäjätunnus on väärä")

    login_user(user)
    print("Käyttäjä " + user.nimi + " tunnistettiin")
    return redirect(url_for("index"))  


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/kasvattaja/lisaa/")
def kasvattaja_lomake():
    return render_template("auth/lisaakasvattaja.html", form = BreederForm())

@app.route("/kasvattaja/lisaa/", methods=["POST"])
def kasvattaja_lisaa():
    form = BreederForm(request.form)

    if not form.validate():
        return render_template("auth/lisaakasvattaja.html", form = form)

    t = User(request.form.get("nimi"), request.form.get("username"), request.form.get("password"), request.form.get("yhteyshlo"), 'USER')

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

@app.route("/kasvattajat", methods=["GET"])
def kasvattaja_index():
    return render_template("auth/kasvattajalista.html", kasvattajat = User.query.all())