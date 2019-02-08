from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application import db
from sqlalchemy.sql import text


class AnimalForm(FlaskForm):
    nimi = StringField("Eläimen nimi", [validators.Length(min=2, max=200)])
    sukupuoli = SelectField(u'Sukupuoli', choices=[('uros', 'uros'), ('naaras', 'naaras')])
    varitys = StringField("Väritys", [validators.Length(max=200)])
    rotu = StringField("Rotu", [validators.Length(max=200)])

    class Meta:
        csrf = False


@staticmethod
def listaa_rodut():
    stmt = text("SELECT Rotu.id, Rotu.nimi FROM Rotu")
    res = db.engine.execute(stmt)

    for row in res:
        print(row[0])
        print(row[1])
