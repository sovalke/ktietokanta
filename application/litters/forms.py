from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateField
from application import db
from sqlalchemy.sql import text
from application.auth.models import User
from application.animals.models import Elain


class LitterForm(FlaskForm):
    nimi = StringField("Pentueen nimi", [validators.Length(min=2, max=200)])
    syntynyt = DateField("Syntymäaika", [validators.Length(min=10, max=11)])    
    
    kasvattaja = SelectField( u'Kasvattaja', 
        choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')],
        coerce=int
    )



    class Meta:
        csrf = False
