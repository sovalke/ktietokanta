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

stmt = text("INSERT INTO kasvattaja (nimi, username, password, yhteyshlo) VALUES ('hello world', 'hello', 'world', 'John Smith')")
db.engine.execute(stmt)

from application.creatures import models 
from application.creatures import views

try: 
    db.create_all()
except:
    pass