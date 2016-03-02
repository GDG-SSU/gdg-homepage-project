from . import admin, db

from .models import UserDB, UserProfile, PortFolio

__author__ = 'Genus'

from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(UserDB, db.session))
admin.add_view(ModelView(UserProfile, db.session))
admin.add_view(ModelView(PortFolio, db.session))

