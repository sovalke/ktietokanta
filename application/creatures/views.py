from application import app, db
from flask import redirect, render_template, request, url_for
from application.creatures.models import Elain
from application.breeds.models import Rotu
from sqlalchemy import update
from flask_login import login_required

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.creatures.forms import CreatureForm

@app.route("/elaimet/lisaa/")
@login_required
def elain_lomake():
    return render_template("creatures/lisaaelain.html", form = CreatureForm())

@app.route("/elaimet/lisaa/", methods=["POST"])
@login_required
def elain_lisaa():
    form = CreatureForm(request.form)

    if not form.validate():
        return render_template("creatures/lisaaelain.html", form = form)

    print( request.form )

    t = Elain(
        request.form.get("nimi"),
        request.form.get("sukupuoli"),
        request.form.get("varitys"),
        request.form.get("rotu_id")
    )

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("elain_index"))


@app.route("/elaimet", methods=["GET"])
def elain_index():
    return render_template("creatures/elainlista.html", elaimet = Elain.query.all())