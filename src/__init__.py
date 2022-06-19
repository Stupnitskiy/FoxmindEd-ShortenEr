import os

from flask import Flask

app = Flask("FoxmindEd ShortenEr", template_folder='src/templates')

app.config.from_object('src.configs.dev')
app.config['FLASK_ENV'] = 'development'
app.secret_key = os.urandom(24)
