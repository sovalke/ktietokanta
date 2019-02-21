from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from sqlalchemy import update
from flask_login import current_user
from sqlalchemy.sql import text

from application import app
from application.breeds.models import Rotu
from application.auth.models import User
from application.auth.forms import LoginForm
from application.animals.forms import AnimalForm
from application.animals.models import Elain

@app.route("/elaimet/lisaa/")
@login_required()
def elain_lomake():
    form = AnimalForm()
    form.rotu.choices = [(g.id, g.nimi) for g in Rotu.query.order_by('nimi')]

    return render_template("animals/lisaaelain.html", form = form)

@app.route("/elaimet/lisaa/", methods=["POST"])
@login_required()
def elain_lisaa():
    form = AnimalForm(request.form)
    form.rotu.choices = [(g.id, g.nimi) for g in Rotu.query.order_by('nimi')]
    if not form.validate():
        return render_template("animals/lisaaelain.html", form = form)

    print( request.form )

    t = Elain(
        request.form.get("nimi"),
        request.form.get("sukupuoli"),
        request.form.get("varitys"),
        request.form.get("rotu")
    )

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("elain_index"))


@app.route("/elaimet", methods=["GET"])
def elain_index():
    stmt = text("SELECT Elain.id, Elain.nimi, Elain.sukupuoli, Elain.varitys, Rotu.id AS rotu_id, Rotu.nimi AS rotu_nimi, Rotu.linja"
    " FROM Elain"
    " LEFT JOIN Rotu ON Rotu.id = Elain.rotu")
    res = db.engine.execute(stmt)
    return render_template("animals/elainlista.html", elaimet = res)