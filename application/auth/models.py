from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "kasvattaja"
  
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    yhteyshlo = db.Column(db.String(200), nullable=True)
    puh = db.Column(db.String(20), nullable=True)
    email= db.Column(db.String(200), nullable=True)
    osoite = db.Column(db.String(200), nullable=True)
    postinro = db.Column(db.String(5), nullable=True)
    toimipaikka = db.Column(db.String(200), nullable=True)
    role = db.Column(db.String(20))

    def __init__(self, nimi, username, password, yhteyshlo, role):
        self.nimi = nimi
        self.username = username
        self.password = password
        self.yhteyshlo = yhteyshlo
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return [self.role]

    # Listataan kasvattajat
    @staticmethod
    def kasvattajaLista():
        stmt = text("SELECT nimi,"
        " (SELECT count(*) FROM Pentue WHERE Pentue.kasvattaja = Kasvattaja.id)"
        " AS pentueita,"
        " (SELECT count(*) FROM Pennut WHERE Pentue IN"
        " (SELECT id FROM Pentue WHERE Kasvattaja = Kasvattaja.id))"
        " AS pentuja,"
        " Kasvattaja.id AS kasvattaja_id" 
        " FROM Kasvattaja")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({
                "nimi": row[0], 
                "pentueita": row[1], 
                "pentuja": row[2],
                "rodut": haeRodutKasvattajalle(row[3])
            })

        return response


# Metodi, joka listaa kaikki rodut tietylle kasvattajalle
def haeRodutKasvattajalle(kasvattaja_id):
    stmt = text("select distinct rotu.nimi as rotu "
    " from Rotu"
    " left join Elain on elain.rotu = rotu.id"
    " left join pennut on pennut.elain = elain.id"
    " left join pentue on pentue.id = pennut.pentue"
    " left join kasvattaja on kasvattaja.id = pentue.kasvattaja"
    " where kasvattaja.id = :kasvattaja_id").params(kasvattaja_id=kasvattaja_id)

    res = db.engine.execute(stmt)

    response = []
    for row in res:
        response.append({"nimi": row[0]})

    return response