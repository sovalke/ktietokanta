from application import app, db
from flask import redirect, render_template, request, url_for
from application.animals.models import Elain
from sqlalchemy import update
from flask_login import login_required

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.animals.forms import AnimalForm

@app.route("/elaimet/lisaa/")
@login_required
def elain_lomake():
    return render_template("animals/lisaaelain.html", form = AnimalForm())

@app.route("/elaimet/lisaa/", methods=["POST"])
@login_required
def elain_lisaa():
    form = AnimalForm(request.form)

    if not form.validate():
        return render_template("animals/lisaaelain.html", form = form)

    t = Elain(request.form.get("nimi"), request.form.get("sukupuoli"), request.form.get("varitys"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("rotu_index"))