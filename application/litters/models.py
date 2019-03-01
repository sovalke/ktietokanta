from application import db
from application.models import Base
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

association_table = Table('pennut', Base.metadata,
    Column('elain', Integer, ForeignKey('elain.id')),
    Column('pentue', Integer, ForeignKey('pentue.id'))
)

class Pentue(Base):

    __tablename__ = "pentue"

    syntynyt = db.Column(db.Date)
    kasvattaja = db.Column(db.Integer, db.ForeignKey('kasvattaja.id'),
                           nullable=True)
    pennut = relationship("Elain",
                    secondary=association_table)
    isa = db.Column(db.Integer, db.ForeignKey('elain.id'),
                           nullable=True)
    ema = db.Column(db.Integer, db.ForeignKey('elain.id'),
                           nullable=True)

    def __init__(self, nimi, syntynyt, kasvattaja, isa, ema):
        self.nimi = nimi
        self.syntynyt = syntynyt
        self.kasvattaja = kasvattaja
        self.isa = isa
        self.ema = ema

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    # Haetaan ltietyn pentueen eläimet.
    @staticmethod
    def haeLista(pentue_id):
        stmt = text("select distinct rotu.nimi as rotu, elain.nimi as elain_nimi, elain.sukupuoli "
        " from Rotu"
        " left join Elain on elain.rotu = rotu.id"
        " left join pennut on pennut.elain = elain.id"
        " left join pentue on pentue.id = pennut.pentue"
        " where pentue.id = :pentue_id").params(pentue_id=pentue_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"rotu": row[0], "nimi": row[1], "sukupuoli": row[2]})

        return response

    # Haetaan lista kaikista pentueista.
    @staticmethod
    def haePentueet():
        stmt = text("SELECT Pentue.id, Pentue.nimi, Pentue.syntynyt,"
        " Kasvattaja.id as kasvattaja_id, Kasvattaja.nimi AS kasvattaja_nimi"
        " FROM Pentue, Kasvattaja WHERE Pentue.kasvattaja = Kasvattaja.id")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({
                "id": row[0],
                "nimi": row[1],
                "syntynyt": row[2], 
                "kasvattaja_id": row[3],
                "kasvattaja_nimi": row[4]
            })

        return response
