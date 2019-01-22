from application import db

class Rotu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    linja = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi, linja):
        self.nimi = nimi
        self.linja = linja