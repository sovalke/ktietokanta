from application import db
from application.models import Base
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

association_table = Table('ElainPentue', Base.metadata,
    Column('elain', Integer, ForeignKey('elain.id')),
    Column('pentue', Integer, ForeignKey('pentue.id'))
)

class Pentue(Base):

    __tablename__ = "Pentue"

    syntynyt = db.Column(db.Date)
    kasvattaja = db.Column(db.Integer, db.ForeignKey('kasvattaja.id'),
                           nullable=True)
    pennut = relationship("Elain",
                    secondary=association_table)

    def __init__(self, nimi, syntynyt, kasvattaja):
        self.nimi = nimi
        self.syntynyt = syntynyt
        self.kasvattaja = kasvattaja

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True