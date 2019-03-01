from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_login import login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, BreederForm
from sqlalchemy.sql import text


# Sisäänkirjautuminen
@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/kirjautuminen.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/kirjautuminen.html", form=form,
                               error="Salasana tai käyttäjätunnus on väärä")

    login_user(user)
    print("Käyttäjä " + user.nimi + " tunnistettiin")
    return redirect(url_for("index"))

# Uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# Rekisteröityminen
@app.route("/kasvattaja/lisaa/")
def kasvattaja_lomake():
    return render_template("auth/lisaakasvattaja.html", form=BreederForm())

# Rekisteröityminen
@app.route("/kasvattaja/lisaa/", methods=["POST"])
def kasvattaja_lisaa():
    form = BreederForm(request.form)

    if not form.validate():
        return render_template("auth/lisaakasvattaja.html", form=form)

    uusiKasvattaja = User(request.form.get("nimi"), request.form.get("username"),
             request.form.get("password"), request.form.get("yhteyshlo"), 'USER')

    db.session().add(uusiKasvattaja)
    db.session().commit()

    return redirect(url_for("rotu_index"))

# Tietojen muokkaus
@app.route("/kasvattaja/<kasvattaja>/muokkaa/", methods=["POST"])
def kasvattaja_muokkaa(kasvattaja):
    form = BreederForm(request.form)

    kasiteltava = User.query.get(kasvattaja)
    kasiteltava.nimi = request.form.get("nimi")
    kasiteltava.username = request.form.get("username")
    kasiteltava.password = request.form.get("password")
    kasiteltava.yhteyshlo = request.form.get("yhteyshlo")
    kasiteltava.puh = request.form.get("puh")
    kasiteltava.email = request.form.get("email")
    kasiteltava.osoite = request.form.get("osoite")
    kasiteltava.postinro = request.form.get("postinro")
    kasiteltava.toimipaikka = request.form.get("toimipaikka")

    if not form.validate():
        return render_template("auth/kasvattaja_muokkaus.html", kasvattaja=kasiteltava, form=form)

    db.session().commit()

    return redirect(url_for("kasvattaja_index"))

# Tietojen muokkaus
@app.route("/kasvattaja/<kasvattaja_id>/muokkaa/", methods=["GET"])
@login_required
def kasvattaja_muokkaa_yksi(kasvattaja_id):
    if current_user.id != int(kasvattaja_id):
        return "Sinulla ei ole oikeuksia lukea tätä."
    
    kasvattaja = User.query.get(kasvattaja_id)

    if request.method == 'GET':
        form = BreederForm(obj=kasvattaja)
    else:
        form = BreederForm(request.form)
        kasvattaja.nimi = request.form.get("nimi")
        kasvattaja.username = request.form.get("username")
        kasvattaja.password = request.form.get("password")
        kasvattaja.yhteyshlo = request.form.get("yhteyshlo")
        kasvattaja.puh = request.form.get("puh")
        kasvattaja.email = request.form.get("email")
        kasvattaja.osoite = request.form.get("osoite")
        kasvattaja.postinro = request.form.get("postinro")
        kasvattaja.toimipaikka = request.form.get("toimipaikka")

    if not form.validate():
        return render_template("auth/kasvattaja_muokkaus.html", form=form, kasvattaja=kasvattaja)

    return render_template("auth/kasvattaja_muokkaus.html", kasvattaja=kasvattaja, form=form)

# Kasvattajalistaus
@app.route("/kasvattajat", methods=["GET"])
def kasvattaja_index():

    return render_template("auth/kasvattajalista.html", kasvattajat=User.kasvattajaLista())
