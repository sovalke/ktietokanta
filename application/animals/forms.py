from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AnimalForm(FlaskForm):
    nimi = StringField("Eläimen nimi", [validators.Length(min=2, max=200)])
    sukupuoli = StringField("Sukupuoli", [validators.Length(min=2, max=200)])
    varitys= StringField("Väritys", [validators.Length(max=200)])
    kasvattaja = StringField("Kasvattaja", [validators.Length(max=200)])
 
    class Meta:
        csrf = False