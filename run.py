#!venv/bin/python
import os

from src import app
from src import views, models

os.environ["FLASK_ENV"] = 'development'

if __name__ == '__main__':
    app.run(
        debug=app.config["DEBUG"],
        host=app.config["HOST"],
        port=app.config["PORT"]
    )
