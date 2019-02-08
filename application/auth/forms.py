from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False


class BreederForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    nimi = StringField("Kasvattajanimi")
    admin = BooleanField(false_values=None)

    class Meta:
        csrf = False