from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application import db
from sqlalchemy.sql import text
from application.breeds.models import Rotu


class AnimalForm(FlaskForm):
    nimi = StringField("Eläimen nimi", [validators.Length(min=2, max=200)])
    sukupuoli = SelectField(u'Sukupuoli', choices=[
                            ('uros', 'uros'), ('naaras', 'naaras')])
    varitys = StringField("Väritys", [validators.Length(max=200)])    
    
    rotu = SelectField( u'Rotu', coerce=int)

# Tähän tulee viite pentueeseen.

    class Meta:
        csrf = False
