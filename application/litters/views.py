from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.animals.models import Elain
from application.breeds.models import Rotu
from application.litters.models import Pentue
from sqlalchemy import update
from sqlalchemy.sql import text

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.litters.forms import LitterForm

from datetime import datetime, date

@app.route("/pentueet/lisaa/")
@login_required()
def pentue_lomake():
    return render_template("litters/lisaapentue.html", form = LitterForm())

@app.route("/pentueet/lisaa/", methods=["POST"])
@login_required()
def pentue_lisaa():
    form = LitterForm(request.form)

    if not form.validate():
        return render_template("litters/lisaapentue.html", form = form)

    print( request.form )

    pvm = datetime.strptime(request.form.get("syntynyt"), '%d.%m.%Y').date()

    t = Pentue(
        request.form.get("nimi"),
        pvm,
        request.form.get("kasvattaja")
    )

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))


@app.route("/pentueet", methods=["GET"])
def pentue_index():
    stmt = text("SELECT Pentue.id, Pentue.nimi, Pentue.kasvattaja AS kasvattaja_id, Pentue.syntynyt, Kasvattaja.id, Kasvattaja.nimi AS kasvattaja_nimi FROM Pentue, Kasvattaja WHERE Pentue.kasvattaja = Kasvattaja.id")
    res = db.engine.execute(stmt)
    return render_template("litters/pentuelista.html", pentueet = res)