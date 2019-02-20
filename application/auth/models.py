from application import db
from application.models import Base

class User(Base):

    __tablename__ = "kasvattaja"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    yhteyshlo = db.Column(db.String(144), nullable=True)
    puh = db.Column(db.String(144), nullable=True)
    email= db.Column(db.String(144), nullable=True)
    osoite = db.Column(db.String(200), nullable=True)
    postinro = db.Column(db.String(5), nullable=True)
    toimipaikka = db.Column(db.String(144), nullable=True)
    role = db.Column(db.String(80))

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
        return self.role