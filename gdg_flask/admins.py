__author__ = 'Genus'
# flask-admin ModelView
from flask_admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin

# 파일업로드를 위함
import os.path as op

# custom
from . import admin, db
from .models import UserDB, UserProfile, PortFolio, ProfileRibbon, ProfileSocial

admin.add_view(ModelView(UserDB, db.session))
admin.add_view(ModelView(UserProfile, db.session))
admin.add_view(ModelView(PortFolio, db.session))
admin.add_view(ModelView(ProfileRibbon, db.session))
admin.add_view(ModelView(ProfileSocial, db.session))


path = op.join(op.dirname(__file__), 'media')
admin.add_view(FileAdmin(path, '/media/', name='Media Files'))
