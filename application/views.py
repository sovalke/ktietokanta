from flask import render_template
from application import app, db
from sqlalchemy.sql import text
from application.models import Base

@app.route("/")
def index():
    return render_template("index.html", tilasto = Base.tilasto())