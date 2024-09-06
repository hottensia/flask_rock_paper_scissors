import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///rockpaperscissors.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


CACHE_TYPE = "SimpleCache"
CACHE_DEFAULT_TIMEOUT = 300

APP_NAME = "rock_paper_scissors"