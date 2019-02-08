from flask_wtf import FlaskForm
from wtforms import StringField, validators
from sqlalchemy.sql import text
from application import db


class BreedForm(FlaskForm):
    nimi = StringField("Rodun nimi", [validators.Length(min=2, max=200)])
    linja = StringField("Jalostuslinja", [validators.Length(max=200)])

    class Meta:
        csrf = False


@staticmethod
def listaa():
    stmt = text("SELECT Rotu.id, Rotu.nimi FROM Account")
    res = db.engine.execute(stmt)

    for row in res:
        print(row[0])
        print(row[1])
