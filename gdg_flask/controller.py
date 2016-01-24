from flask import render_template
from gdg_flask import app


@app.route('/')
def home():
    return render_template("gdg-article/home.html")



# @app.route('/temp12')
# def temp12():
#     return render_template("base/layout.html")
