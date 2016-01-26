import os
from datetime import timedelta

"""
settings.py

Configuration for Flask app

"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPS_DIR = os.path.join(BASE_DIR, 'gdg_flask')


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "_kindlaw_at_genus_"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=50)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://gdg_ssu@52.11.192.101/GDGSSU?charset=utf8"
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # UPLOAD_FOLDER =

class Production(Config):
    CSRF_ENABLED = False
    ADMIN = "jackok12@naver.com"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<user_id>@<host>/<DB name>?charset=utf8"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=40)
    migration_directory = 'migrations'



class Develop(Config):
    DEBUG = True
    CSRF_ENABLED = False
    ADMIN = "jackok12@gmail.com"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=100)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI =
    migration_directory = 'migrations'


