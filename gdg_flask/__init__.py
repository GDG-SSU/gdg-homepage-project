from flask import Flask
from flask.ext.admin import Admin
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('apps.settings.Develop')
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

admin = Admin(app)

from gdg_flask import controller, models, admins
