from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_login import login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, BreederForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/kirjautuminen.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/kirjautuminen.html", form=form,
                               error="Salasana tai käyttäjätunnus on väärä")

    login_user(user)
    print("Käyttäjä " + user.nimi + " tunnistettiin")
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/kasvattaja/lisaa/")
def kasvattaja_lomake():
    return render_template("auth/lisaakasvattaja.html", form=BreederForm())


@app.route("/kasvattaja/lisaa/", methods=["POST"])
def kasvattaja_lisaa():
    form = BreederForm(request.form)

    if not form.validate():
        return render_template("auth/lisaakasvattaja.html", form=form)

    t = User(request.form.get("nimi"), request.form.get("username"),
             request.form.get("password"), request.form.get("yhteyshlo"), 'USER')

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("rotu_index"))


# Vain kasvattaja itse voi muokata omia tietojaan
@app.route("/kasvattajat/<kasvattaja>/muokkaa/", methods=["POST"])
def kasvattaja_muokkaa(kasvattaja):
    form = BreederForm(request.form)

    t = User.query.get(kasvattaja)
    t.nimi = request.form.get("nimi")
    t.username = request.form.get("username")
    t.password = request.form.get("password")
    t.yhteyshlo = request.form.get("yhteyshlo")
    t.puh = request.form.get("puh")
    t.email = request.form.get("email")
    t.osoite = request.form.get("osoite")
    t.postinro = request.form.get("postinro")
    t.toimipaikka = request.form.get("toimipaikka")

    if not form.validate():
        return render_template("auth/kasvattaja_muokkaus.html", kasvattaja=t, form=form)

    db.session().commit()

    return redirect(url_for("kasvattaja_index"))

@app.route("/kasvattajat/<kasvattaja_id>/muokkaa/", methods=["GET"])
#@tarkistakayttaja(kasvattaja)
@login_required
def kasvattaja_muokkaa_yksi(kasvattaja_id):
    if current_user.id != int(kasvattaja_id):
        return "sinulla ei ole oikeuksia lukea tätä ja me tyylitellään tämä sivu myöhemmin hienoksi"
    

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


@app.route("/kasvattajat", methods=["GET"])
def kasvattaja_index():
    return render_template("auth/kasvattajalista.html", kasvattajat=User.query.all())
