from application import app, db
from flask import redirect, render_template, request, url_for
from application.animals.models import Elain
from sqlalchemy import update
from flask_login import login_required

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm