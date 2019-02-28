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

# Uuden pentueen lisääminen
@app.route("/pentueet/lisaa/")
@login_required()
def pentue_lomake():
    form = LitterForm()
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]

    return render_template("litters/lisaapentue.html", form = form)

# Uuden pentueen lisääminen
@app.route("/pentueet/lisaa/", methods=["POST"])
@login_required()
def pentue_lisaa():
    form = LitterForm(request.form)
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]

    if not form.validate():
        return render_template("litters/lisaapentue.html", form = form)

    pvm = datetime.strptime(request.form.get("syntynyt"), '%d.%m.%Y').date()
    lisattava = Pentue(request.form.get("nimi"), pvm, request.form.get("kasvattaja"), request.form.get("isa"), request.form.get("ema"))

    db.session().add(lisattava)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))

# Pentueen muokkaus
@app.route("/pentueet/<pentue>/muokkaa/", methods=["POST"])
@login_required()
def pentue_muokkaa(pentue):
    form = LitterForm(request.form)
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    muokattava = Pentue.query.get(pentue)

    muokattava.nimi = request.form.get("nimi")
    muokattava.syntynyt = request.form.get("syntynyt")
    muokattava.kasvattaja = request.form.get("kasvattaja")
    muokattava.isa = request.form.get("isa")
    muokattava.ema = request.form.get("ema")
    pvm = datetime.strptime(request.form.get("syntynyt"), '%d.%m.%Y').date()

    muokattava.syntynyt = pvm

    if not form.validate():
        return render_template("litters/pentue_muokkaus.html", pentue = muokattava, form = form)

    db.session().commit()
  
    return redirect(url_for("pentue_yksi", pentue = muokattava.id))

# Pentueen muokkaaminen
@app.route("/pentueet/<pentue>/muokkaa/", methods=["GET"])
@login_required()
def pentue_muokkaa_yksi(pentue):
    form = LitterForm(request.form)
    form.kasvattaja.choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')]
    form.isa.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    form.ema.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    muokattava = Pentue.query.get(pentue)

    if request.method == 'GET':
        form.nimi.data = muokattava.nimi
        form.syntynyt.data = muokattava.syntynyt
        form.kasvattaja.data = muokattava.kasvattaja
        form.isa.data = muokattava.isa
        form.ema.data = muokattava.ema

    if not form.validate():
        return render_template("litters/pentue_muokkaus.html", form = form, pentue = muokattava)

    return render_template("litters/pentue_muokkaus.html", pentue=muokattava, form = form)

# Pennun lisääminen
@app.route("/pentueet/<pentue>/lisaapentu/")
@login_required()
def pentu_lomake(pentue):
    form = PupForm()
    form.pentu.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]
    kasiteltavaPentue = Pentue.query.get(pentue)
    return render_template("litters/lisaapentu.html", pentue = kasiteltavaPentue, form = form)

# Pennun lisääminen
@app.route("/pentueet/<pentue>/lisaapentu/", methods=["POST"])
@login_required()
def pentu_lisaa(pentue):
    form = PupForm(request.form)
    form.pentu.choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')]

    if not form.validate():
        return render_template("litters/lisaapentu.html", form = form)

    lisattava = request.form.get("pentu")
    pentue = Pentue.query.get(pentue)
    pentue.pennut.append(Elain.query.get(lisattava))

    db.session().commit()
  
    return redirect(url_for("pentue_yksi", pentue = pentue.id))

# Pentueen poistaminen
@app.route("/pentueet/poista<pentue_id>/", methods=["POST"])
@login_required(role="ADMIN")
def pentue_poista(pentue_id):
    poistettava = Pentue.query.get(pentue_id)
    db.session.delete(poistettava)
    db.session().commit()
  
    return redirect(url_for("pentue_index"))

# Pentuelistaus
@app.route("/pentueet", methods=["GET"])
def pentue_index():
    stmt = text("SELECT Pentue.id, Pentue.nimi, Pentue.syntynyt, Kasvattaja.id as kasvattaja_id, Kasvattaja.nimi AS kasvattaja_nimi FROM Pentue, Kasvattaja WHERE Pentue.kasvattaja = Kasvattaja.id")
    res = db.engine.execute(stmt)
    return render_template("litters/pentuelista.html", pentueet = res)

# Yksittäisen pentueen tarkastelu
@app.route("/pentueet/<pentue>/", methods=["GET"])
def pentue_yksi(pentue):
    pentue = Pentue.query.get(pentue)
    ema = Elain.query.get(pentue.ema)
    isa = Elain.query.get(pentue.isa)
    kasvattaja = User.query.get(pentue.kasvattaja)

    return render_template("litters/pentue.html", pentue = pentue, ema = ema, isa = isa, kasvattaja = kasvattaja)

