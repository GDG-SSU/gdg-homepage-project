from flask import Blueprint, render_template

from .python_modules.parsing import FileParser


# import current_app models
from gdg_flask.models import UserProfile


recruits_201601 = Blueprint('recruits_201601', __name__, template_folder='templates', static_folder='static',
                            url_prefix='/about/recruits/201601')



@recruits_201601.route('/')
def recruit_index():
    members = UserProfile.query.limit(4).all()

    return render_template('recruits_contents.html', members=members)

