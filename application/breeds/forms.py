from flask_wtf import FlaskForm
from wtforms import StringField, validators

class BreedForm(FlaskForm):
    nimi = StringField("Rodun nimi", [validators.Length(min=2, max=200)])
    linja = StringField("Jalostuslinja", [validators.Length(max=200)])
 
    class Meta:
        csrf = False