from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from sqlalchemy import update

from application.breeds.forms import BreedForm
from application.breeds.models import Rotu

# Vain ylläpitäjä voi lisätä uusia rotuja.
@app.route("/rodut/lisaa/")
@login_required(role="ADMIN")
def rotu_lomake():
    return render_template("breeds/lisaarotu.html", form = BreedForm())

# Vain ylläpitäjä voi lisätä uusia rotuja.
@app.route("/rodut/lisaa/", methods=["POST"])
@login_required(role="ADMIN")
def rotu_lisaa():
    form = BreedForm(request.form)

    if not form.validate():
        return render_template("breeds/lisaarotu.html", form = form)

    t = Rotu(request.form.get("nimi"), request.form.get("linja"), request.form.get("kuvaus"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi poistaa rotuja.
@app.route("/rodut/poista<rotu>/", methods=["POST"])
@login_required(role="ADMIN")
def rotu_poista(rotu):
    poistettava = Rotu.query.get(rotu)
    db.session.delete(poistettava)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi muokata rotuja.
@app.route("/rodut/<rotu>/", methods=["POST"])
@login_required(role="ADMIN")
def rotu_muokkaa(rotu):
    form = BreedForm(request.form)
    t = Rotu.query.get(rotu)
    t.nimi = request.form.get("nimi")
    t.linja = request.form.get("linja")
    t.kuvaus = request.form.get("kuvaus")

    if not form.validate():
        return render_template("breeds/rotu_muokkaus_yksi.html", rotu = t, form = form)

    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi muokata rotuja.
@app.route("/rodut/muokkaa/<rotu>/", methods=["GET"])
@login_required(role="ADMIN")
def rotu_muokkaa_yksi(rotu):
    form = BreedForm(request.form)
    t = Rotu.query.get(rotu)

    if request.method == 'GET':
        form.nimi.data = t.nimi
        form.linja.data = t.linja

    if not form.validate():
        return render_template("breeds/rotu_muokkaus_yksi.html", form = form, rotu = t)

    return render_template("breeds/rotu_muokkaus_yksi.html", rotu=t, form = form)


@app.route("/rodut", methods=["GET"])
def rotu_index():
    return render_template("breeds/rotulista.html", rodut = Rotu.query.all())
  