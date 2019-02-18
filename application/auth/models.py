from application import db
from application.models import Base

class User(Base):

    __tablename__ = "kasvattaja"
  
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    yhteyshlo = db.Column(db.String(144), nullable=False)
    puh = db.Column(db.String(144), nullable=False)
    email= db.Column(db.String(144), nullable=False)
    osoite = db.Column(db.String(200), nullable=False)
    postinro = db.Column(db.String(5), nullable=False)
    toimipaikka = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi, username, password, email):
        self.nimi = nimi
        self.username = username
        self.password = password
        self.email = email
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True