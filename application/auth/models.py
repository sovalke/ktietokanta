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

    @staticmethod
    def kasvattajaLista():
        stmt = text("SELECT nimi,"
        " (SELECT count(*) FROM Pentue WHERE Pentue.kasvattaja = Kasvattaja.id)"
        " AS pentueita,"
        " (SELECT count(*) FROM Pennut WHERE Pentue IN"
        " (SELECT id FROM Pentue WHERE Kasvattaja = Kasvattaja.id))"
        " AS pentuja" 
        " FROM Kasvattaja")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"nimi": row[0], 
            "pentueita": row[1], 
            "pentuja": row[2]})

        return response