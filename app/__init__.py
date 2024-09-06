import logging
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

""" 
Logging configuration 
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s%(name)s:%(message)s")
logging.getLogger().setLevel(logging.ERROR)

app = Flask(__name__)

app.config.from_object("config")

db = SQLAlchemy(app)

api = Api(app, db.session)