from application import app, db
from flask import redirect, render_template, request, url_for
from application.breeds.models import Rotu
from sqlalchemy import update
from application.breeds.forms import BreedForm
from flask_login import login_required


@app.route("/rodut/lisaa/")
@login_required
def rotu_lomake():
    return render_template("breeds/lisaarotu.html", form = BreedForm())

@app.route("/rodut/lisaa/", methods=["POST"])
@login_required
def rotu_lisaa():
    form = BreedForm(request.form)

    if not form.validate():
        return render_template("breeds/lisaarotu.html", form = form)

    t = Rotu(request.form.get("nimi"), request.form.get("linja"))

    db.session().add(t)
    db.session().commit()
    db.session().flush()
  
    return redirect(url_for("rotu_index"))

@app.route("/rodut/poista<rotu>/", methods=["POST"])
@login_required
def rotu_poista(rotu):
    poistettava = Rotu.query.get(rotu)
    db.session.delete(poistettava)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

@app.route("/rodut/<rotu>/", methods=["POST"])
@login_required
def rotu_muokkaa(rotu):
    form = BreedForm(request.form)
    t = Rotu.query.get(rotu)
    t.nimi = request.form.get("nimi")
    t.linja = request.form.get("linja")

    if not form.validate():
        return render_template("breeds/rotu_muokkaus_yksi.html", rotu = t, form = form)

    db.session().commit()
  
    return redirect(url_for("rotu_index"))

@app.route("/rodut/muokkaa/<rotu>/", methods=["GET"])
@login_required
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
  