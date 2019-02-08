from application import db
from application.models import Base

class Elain(Base):

    __tablename__ = "elain"
  
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    sukupuoli = db.Column(db.String(144), nullable=False)
    varitys = db.Column(db.String(144), nullable=False)
    rotu_id = db.Column(db.Integer, db.ForeignKey('rotu.id'),
                           nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True