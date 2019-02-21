from application import db
from application.models import Base

class Elain(Base):

    __tablename__ = "Elain"

    sukupuoli = db.Column(db.String(144), nullable=False)
    varitys = db.Column(db.String(144), nullable=False)
    rotu = db.Column(db.Integer, db.ForeignKey('rotu.id'),
                           nullable=True)

    def __init__(self, nimi, sukupuoli, varitys, rotu):
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.varitys = varitys
        self.rotu = rotu
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True
