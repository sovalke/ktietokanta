from application import db
from sqlalchemy.sql import text


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(200), nullable=False)


    @staticmethod
    def tilasto():
        stmt = text("SELECT COUNT(DISTINCT Kasvattaja.id) AS kasvattaja,"
                    " COUNT(DISTINCT Pentue.id) AS pentue,"
                    " COUNT(DISTINCT Elain.id) AS elain,"
                    " COUNT(DISTINCT Rotu.id) AS rotu"
                    " FROM Kasvattaja, Pentue, Elain, Rotu")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kasvattaja": row[0], "pentue": row[1], "elain": row[2], "rotu": row[3]})

        return response
