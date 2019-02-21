from application import db
from application.models import Base
from sqlalchemy.sql import text

class Rotu(Base):
    __tablename__ = "Rotu"

    linja = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.String(500))

    def __init__(self, nimi, linja, kuvaus):
        self.nimi = nimi
        self.linja = linja
        self.kuvaus = kuvaus

    def get_nimi(self):
        return self.nimi