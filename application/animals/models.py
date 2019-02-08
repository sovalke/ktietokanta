from application import db
from application.models import Base

class Elain(Base):

    __tablename__ = "elain"
  
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    sukupuoli = db.Column(db.String(144), nullable=False)
    varitys = db.Column(db.String(144), nullable=False)
    rotu_id = db.Column(db.Integer, db.ForeignKey('rotu.id'),
                           nullable=True)

    def __init__(self, nimi, sukupuoli, varitys, rotu_id):
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.varitys = varitys
        self.rotu_id = rotu_id
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True
