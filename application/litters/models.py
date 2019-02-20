from application import db
from application.models import Base

class Pentue(Base):

    __tablename__ = "pentue"
  
    syntynyt = db.Column(db.Date)
    kasvattaja = db.Column(db.Integer, db.ForeignKey('kasvattaja.id'),
                           nullable=True)
    isa = db.Column(db.Integer, db.ForeignKey('elain.id'),
                           nullable=True)
    ema = db.Column(db.Integer, db.ForeignKey('elain.id'),
                           nullable=True)

    def __init__(self, nimi, syntynyt):
        self.nimi = nimi
        self.syntynyt = syntynyt
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True