from application import app, db
from flask import redirect, render_template, request, url_for
from application.creatures.models import Elain
from application.breeds.models import Rotu
from application.litters.models import Pentue
from sqlalchemy import update
from flask_login import login_required

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.litters.forms import LitterForm

@app.route("/pentueet/lisaa/")
@login_required
def elain_lomake():
    return render_template("litter/lisaaelain.html", form = LitterForm())

@app.route("/pentueet/lisaa/", methods=["POST"])
@login_required
def elain_lisaa():
    form = LitterForm(request.form)

    if not form.validate():
        return render_template("litters/lisaapentue.html", form = form)

    print( request.form )

    t = Elain(
        request.form.get("nimi"),
        request.form.get("sukupuoli"),
        request.form.get("varitys"),
        request.form.get("rotu")
    )

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))


@app.route("/pentueet", methods=["GET"])
def elain_index():
    return render_template("litters/pentuelista.html", pentueet = Pentue.query.all())