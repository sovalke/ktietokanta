from application import db
from application.models import Base
from sqlalchemy.sql import text

class Elain(Base):

    __tablename__ = "elain"

    sukupuoli = db.Column(db.String(10), nullable=False)
    varitys = db.Column(db.String(200), nullable=False)
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

    # Metodi kaikkien eläinten listaamiseen
    @staticmethod
    def listaaElaimet():
        stmt = text("SELECT Elain.id AS elain_id, Elain.nimi AS elain_nimi,"
        " Elain.sukupuoli AS elain_sukupuoli, Elain.varitys AS elain_varitys, Rotu.id AS rotu_id,"
        " Rotu.nimi AS rotu_nimi, Rotu.linja AS rotu_linja, COUNT(Elain.id) AS elainMaara"
        " FROM Elain"
        " LEFT JOIN Rotu ON Rotu.id = Elain.rotu"
        " GROUP BY Elain.id"
        " ORDER BY rotu_nimi")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"elain_id": row[0], 
            "elain_nimi": row[1], 
            "elain_sukupuoli": row[2], 
            "elain_varitys": row[3],
            "rotu_id": row[4], 
            "rotu_nimi": row[5], 
            "rotu_linja": row[6]})

        return response