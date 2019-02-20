from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.animals.models import Elain
from application.breeds.models import Rotu
from application.litters.models import Pentue
from sqlalchemy import update

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.litters.forms import LitterForm

@app.route("/pentueet/lisaa/")
@login_required()
def pentue_lomake():
    return render_template("litter/lisaapentue.html", form = LitterForm())

@app.route("/pentueet/lisaa/", methods=["POST"])
@login_required()
def pentue_lisaa():
    form = LitterForm(request.form)

    if not form.validate():
        return render_template("litters/lisaapentue.html", form = form)

    print( request.form )

    t = Pentue(
        request.form.get("nimi"),
        request.form.get("syntynyt"),
        request.form.get("kasvattaja")
    )

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))


@app.route("/pentueet", methods=["GET"])
def pentue_index():
    return render_template("litters/pentuelista.html", pentueet = Pentue.query.all())