from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateField
from wtforms.validators import DataRequired
from application import db
from sqlalchemy.sql import text
from application.auth.models import User
from application.animals.models import Elain


class LitterForm(FlaskForm):
    nimi = StringField("Pentueen nimi", [validators.Length(min=2, max=200)])
    syntynyt = DateField("Syntymäaika", format='%d.%m.%Y', validators=[DataRequired(message="Anna syntymäpäivä muodossa pp.kk.vv")])    
    
    kasvattaja = SelectField( u'Kasvattaja', 
        choices = [(g.id, g.nimi) for g in User.query.order_by('nimi')],
        coerce=int
    )
#    isa = SelectField( u'Isä', 
#        choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')],
#        coerce=int
#    )
#    ema = SelectField( u'Emä', 
#        choices = [(g.id, g.nimi) for g in Elain.query.order_by('nimi')],
#        coerce=int
#    )


    class Meta:
        csrf = False
