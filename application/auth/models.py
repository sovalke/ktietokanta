from application import db
from application.models import Base

class User(Base):

    __tablename__ = "kasvattaja"
  
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi, username, password, admin):
        self.nimi = nimi
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True