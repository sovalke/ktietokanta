from flask import Flask
from sqlalchemy.sql import text

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ktietokanta.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Varsinaisen ohjelman tiedot
from application import views
from application.auth import models 
from application.auth import views
from application.breeds import models
from application.breeds import views

# Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään, jotta voit käyttää tätä toimintoa."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
  
try: 
    db.create_all()
except:
    pass

# Taulut, jotka vaativat muiden taulujen olemassaoloa
from application.animals import models 
from application.animals import views
from application.litters import views
from application.litters import models

try: 
    db.create_all()
except:
    pass

# Luodaan demotunnus
stmt = text("SELECT COUNT(*) FROM Kasvattaja")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text("INSERT INTO kasvattaja (nimi, username, password, yhteyshlo) VALUES ('hello world', 'hello', 'world', 'John Smith')")
    res = db.engine.execute(stmt)

# Luodaan ensimmäiset rivit tauluun rotu
stmt = text("SELECT COUNT(*) FROM Rotu")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text("INSERT INTO rotu (nimi, linja) VALUES ('tuntematon', 'tuntematon')")
    res = db.engine.execute(stmt)

# Luodaan ensimmäiset rivit tauluun pentue
stmt = text("SELECT COUNT(*) FROM Pentue")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text("INSERT INTO pentue (nimi) VALUES ('tuntematon')")
    res = db.engine.execute(stmt)

# Luodaan ensimmäiset rivit tauluun elain
stmt = text("SELECT COUNT(*) FROM Elain")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text("INSERT INTO elain (nimi, sukupuoli, varitys) VALUES ('tuntematon', 'tuntematon', 'tuntematon')")
    res = db.engine.execute(stmt)