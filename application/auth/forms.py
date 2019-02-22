from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False


class BreederForm(FlaskForm):
    nimi = StringField("Kasvattajanimi", [validators.Length(min=3, max=200)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3, max=200)])
    password = PasswordField("Salasana", [validators.Length(min=5, max=200)])
    yhteyshlo = StringField("Yhteyshenkilö")
    puh = StringField("Puhelinnumero")
    email = StringField("Sähköpostiosoite")
    osoite = StringField("Katuosoite")
    postinro = StringField("Postinumero")
    toimipaikka = StringField("Postitoimipaikka")

    class Meta:
        csrf = False