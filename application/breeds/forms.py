from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from sqlalchemy.sql import text
from application import db


class BreedForm(FlaskForm):
    nimi = StringField("Rodun nimi", [validators.Length(min=2, max=200)])
    linja = StringField("Jalostuslinja", [validators.Length(max=150)])
    kuvaus = TextAreaField("Kuvaus", [validators.Length(max=500)])

    class Meta:
        csrf = False
