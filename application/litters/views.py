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
from application.litters.forms import LitterForm, PupForm

from datetime import datetime, date

@app.route("/pentueet/lisaa/")
@login_required()
def pentue_lomake():
    form = LitterForm()
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]

    return render_template("litters/lisaapentue.html", form = form)

@app.route("/pentueet/lisaa/", methods=["POST"])
@login_required()
def pentue_lisaa():
    form = LitterForm(request.form)
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]

    if not form.validate():
        return render_template("litters/lisaapentue.html", form = form)

    print( request.form )

    pvm = datetime.strptime(request.form.get("syntynyt"), '%d.%m.%Y').date()

    t = Pentue(request.form.get("nimi"), pvm, request.form.get("kasvattaja"), request.form.get("isa"), request.form.get("ema"))
    t.pennut.append(Elain.query.get(1))
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))

#@app.route("/pentueet/<id>/lisaapentu/")
#@login_required()
#def pentu_lomake(id):
#    form = PupForm()
#    form.pentu.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
#    return render_template("litters/lisaapentu.html", pentue = Pentue.query.get(id), form = form)

#    t.pennut.append(Elain.query.get(1))
#    db.session().add(t)
#    db.session().commit()


@app.route("/pentueet", methods=["GET"])
def pentue_index():
    stmt = text("SELECT Pentue.id, Pentue.nimi, Pentue.syntynyt, Kasvattaja.id as kasvattaja_id, Kasvattaja.nimi AS kasvattaja_nimi FROM Pentue, Kasvattaja WHERE Pentue.kasvattaja = Kasvattaja.id")
    res = db.engine.execute(stmt)
    return render_template("litters/pentuelista.html", pentueet = res)


@app.route("/pentueet/<pentue>/", methods=["GET"])
def pentue_yksi(pentue):
    t = Pentue.query.get(pentue)
    return render_template("litters/pentue.html", pentue = t, ema = Elain.query.get(t.ema), isa = Elain.query.get(t.isa))

