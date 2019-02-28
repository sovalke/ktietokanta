from application import db
from application.models import Base

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
    
    @dynamicmethod
    def find_breeds():
        stmt = text("SELECT DISTINCT Rotu.nimi AS rotu, Kasvattaja.nimi AS kasvattaja FROM Kasvattaja, Pentue, Pennut, Elain, Rotu WHERE Kasvattaja.id = Pentue.kasvattaja AND Pentue.id = Pennut.pentue AND Pennut.elain = Elain.id AND Elain.rotu = Rotu.id AND Kasvattaja.id = 3")
        res = db.engine.execute(stmt)
        
        for row in res:
            print(row[0])
            print(row[1])