from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")


class BreederForm(FlaskForm):
    nimi = StringField("Kasvattajanimi", [validators.Length(min=3, max=200)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3, max=200)])
    password = PasswordField("Salasana", [validators.Length(min=5, max=200)])
    yhteyshlo = StringField("Yhteyshenkilö", [validators.Length(min=4, max=200)])
    puh = StringField("Puhelinnumero", [validators.Length(min=5, max=20)])
    email = StringField("Sähköpostiosoite", [validators.Length(min=10, max=200)])
    osoite = StringField("Katuosoite", [validators.Length(min=5, max=200)])
    postinro = StringField("Postinumero", [validators.Length(min=5, max=5)])
    toimipaikka = StringField("Postitoimipaikka", [validators.Length(min=4, max=200)])

    class Meta:
        csrf = False