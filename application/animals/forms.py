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
    
    rotu_id = SelectField( u'Valitse rotu tästä', 
        choices = [(g.id, g.id) for g in Rotu.query.order_by('nimi')]
    )

    class Meta:
        csrf = False
