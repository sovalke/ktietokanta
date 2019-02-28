from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(200), nullable=False)