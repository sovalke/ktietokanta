from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from sqlalchemy import update

from application.breeds.forms import BreedForm
from application.breeds.models import Rotu
from application.animals.models import Elain

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

    lisattava = Rotu(request.form.get("nimi"), request.form.get("linja"), request.form.get("kuvaus"))

    db.session().add(lisattava)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi poistaa rotuja.
@app.route("/rodut/poista<rotu>/", methods=["POST"])
@login_required(role="ADMIN")
def rotu_poista(rotu):
    poistettava = Rotu.query.get(rotu)

    if poistettava.id == 1:
        return redirect(url_for("rotu_index"))
    
    tyhjennettavatElaimet = Elain.query.filter(Elain.rotu==poistettava.id)

    # Jos rotu poistetaan, asetetaan eläimen roduksi oletusrotu.
    for elain in tyhjennettavatElaimet:
        elain.rotu = 1
        db.session().commit()

    db.session.delete(poistettava)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi muokata rotuja.
@app.route("/rodut/<rotu>/", methods=["POST"])
@login_required(role="ADMIN")
def rotu_muokkaa(rotu):
    form = BreedForm(request.form)
    muokattava = Rotu.query.get(rotu)
    muokattava.nimi = request.form.get("nimi")
    muokattava.linja = request.form.get("linja")
    muokattava.kuvaus = request.form.get("kuvaus")

    if not form.validate():
        return render_template("breeds/rotu_muokkaus_yksi.html", rotu = muokattava, form = form)

    db.session().commit()
  
    return redirect(url_for("rotu_index"))

# Vain ylläpitäjä voi muokata rotuja.
@app.route("/rodut/muokkaa/<rotu>/", methods=["GET"])
@login_required(role="ADMIN")
def rotu_muokkaa_yksi(rotu):
    form = BreedForm(request.form)
    muokattava = Rotu.query.get(rotu)

    if request.method == 'GET':
        form.nimi.data = muokattava.nimi
        form.linja.data = muokattava.linja

    if not form.validate():
        return render_template("breeds/rotu_muokkaus_yksi.html", form = form, rotu = muokattava)

    return render_template("breeds/rotu_muokkaus_yksi.html", rotu=muokattava, form = form)

# Rotulistaus
@app.route("/rodut", methods=["GET"])
def rotu_index():
    return render_template("breeds/rotulista.html", rodut = Rotu.query.all())

# Yksittäisen rodun tarkastelu
@app.route("/rodut/<rotu>/", methods=["GET"])
def rotu_yksi(rotu):
    rotu = Rotu.query.get(rotu)

    return render_template("breeds/rotu.html", rotu = rotu)
  