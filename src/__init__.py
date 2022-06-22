import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask("FoxmindEd ShortenEr", template_folder='src/templates')

app.config.from_object('src.configs.dev')
app.config['FLASK_ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
