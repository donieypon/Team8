import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Message, Mail

db = SQLAlchemy()
login = LoginManager()

def create_app(debug=False, test_config=None):
	app = Flask(__name__)
	app.debug = debug
	app.config.from_object(Config)

	if test_config is None:
		app.config.from_object('config.Config')
	else:
		app.config.from_mapping('config.Config')	

	db.init_app(app)
	login.init_app(app)
	login.login_view = 'login'	

	with app.app_context():
		from . import routes, models
		db.create_all()
		return app


# app = Flask(__name__)
# app.config.from_object(Config)

# bcrypt = Bcrypt(app)

# db = SQLAlchemy(app)

# login = LoginManager(app)

# login.login_view = 'login'

# from app import routes, models
