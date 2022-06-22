#!venv/bin/python
import os

from src import app

os.environ["FLASK_ENV"] = 'development'

if __name__ == '__main__':
    app.run(
        debug=app.config["DEBUG"],
        host=app.config["HOST"],
        port=app.config["PORT"]
    )
