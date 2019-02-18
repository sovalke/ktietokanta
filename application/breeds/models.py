from application import db
from application.models import Base
from sqlalchemy.sql import text


class Rotu(Base):
    __tablename__ = "rotu"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    linja = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi, linja):
        self.nimi = nimi
        self.linja = linja

    def get_nimi(self):
        return self.nimi