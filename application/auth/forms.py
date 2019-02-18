from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False


class BreederForm(FlaskForm):
    nimi = StringField("Kasvattajanimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    yhteyshlo = StringField("Yhteyshenkilö")
    puh = StringField("Puhelinnumero")
    email = StringField("Sähköpostiosoite")
    osoite = StringField("Katuosoite")
    postinro = StringField("Postinumero")
    toimipaikka = StringField("Postitoimipaikka")

    class Meta:
        csrf = False