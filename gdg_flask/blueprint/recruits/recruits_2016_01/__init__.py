from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

recruits_201601 = Blueprint('recruits_201601', __name__, template_folder='templates', static_folder='static',
                            url_prefix='/about/recruits/201601')


@recruits_201601.route('/')
def recruit_index():
    return render_template('recruits_contents.html')


