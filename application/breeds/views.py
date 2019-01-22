from application import app, db
from flask import redirect, render_template, request, url_for
from application.breeds.models import Rotu
from sqlalchemy import update


@app.route("/rodut/lisaa/")
def rotu_lomake():
    return render_template("breeds/lisaarotu.html")

@app.route("/rodut/lisaa/", methods=["POST"])
def rotu_lisaa():
    t = Rotu(request.form.get("nimi"), request.form.get("linja"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

@app.route("/rodut/poista<rotu_id>/", methods=["POST"])
def rotu_poista(rotu_id):
    poistettava = Rotu.query.get(rotu_id)
    db.session.delete(poistettava)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))

@app.route("/rodut/<rotu_id>/", methods=["POST"])
def rotu_muokkaa(rotu_id):

    t = Rotu.query.get(rotu_id)
    t.nimi = request.form.get("nimi")
    t.linja = request.form.get("linja")
    db.session().commit()
  
    return redirect(url_for("rotu_muokkaus_index"))

@app.route("/rodut/muokkaa", methods=["GET"])
def rotu_muokkaus_index():
    return render_template("breeds/rotulista_muokkaus.html", rodut = Rotu.query.all())

@app.route("/rodut", methods=["GET"])
def rotu_index():
    return render_template("breeds/rotulista.html", rodut = Rotu.query.all())
  