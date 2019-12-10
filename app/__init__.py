import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Message, Mail

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

login = LoginManager(app)

login.login_view = 'login'

from app import routes, models
