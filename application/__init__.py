from flask import Flask
from sqlalchemy.sql import text

app = Flask(__name__)

# Tietokanta ja ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ktietokanta.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Kirjautumistoiminnot 1
from os import urandom
from application.auth.models import User
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Vain kirjautuneet käyttäjät voivat käyttää tätä toimintoa."


# Käyttäjäroolit / login_required
from functools import wraps
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated():
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# Varsinaisen ohjelman tiedot
from application import views
from application.auth import models 
from application.auth import views
from application.breeds import models
from application.breeds import views

try:
    db.create_all()
except:
    pass

# Varsinaisen ohjelman tiedot jatkuvat
from application.animals import models 
from application.animals import views
from application.litters import views
from application.litters import models

try:
    db.create_all()
except:
    pass


# Kirjautumistoiminnot 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Luodaan demotunnus
stmt = text("SELECT COUNT(*) FROM Kasvattaja")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text(
        "INSERT INTO kasvattaja (nimi, username, password, yhteyshlo, role) VALUES ('hello world', 'hello', 'world', 'John Smith', 'ADMIN')")
    res = db.engine.execute(stmt)

# Luodaan ensimmäiset rivit tauluun rotu
stmt = text("SELECT COUNT(*) FROM Rotu")
res = db.engine.execute(stmt).scalar()

if res == 0:
    stmt = text("INSERT INTO rotu (nimi, linja) VALUES ('määrittelemätön', '')")
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
    stmt = text(
        "INSERT INTO elain (nimi, sukupuoli, varitys, rotu) VALUES ('Testieläin', 'naaras', 'tuntematon', '1')")
    res = db.engine.execute(stmt)
