from flask import render_template, url_for, redirect, request
from gdg_flask import app, db
from gdg_flask.forms import UserForm

from .models import UserDB


@app.route('/')
def home():
    return render_template("gdg-article/home.html")

# URL Prefix '/about' is
# about ourselves(gdg-ssu)
# So, if you want to make URL and template resource about GDG-SSU
# You have to post url Prefix '/about' and template resource path to '/templates/gdg-article/about/*'
@app.route('/about')
@app.route('/about/intro')
def about_intro():
    return render_template('gdg-article/about/intro.html')


@app.route('/about/members')
def about_members():
    return render_template('gdg-article/about/members.html')


@app.route('/about/activities')
def about_activities():
    return render_template('gdg-article/about/activities.html')


@app.route('/about/recruits')
def about_recruits():
    return render_template('gdg-article/about/recruits.html')


# URL Prefix '/account' is
# about User Account (login, logout, register.. and so on)
# So, if you want to make URL and template resource about User Account
# You have to post url Prefix '/account' and template resource path to '/templates/gdg-article/account/*'

@app.route('/account/register')
def account_register():
    return render_template('gdg-article/account/register.html')

@app.route('/account/login')
def account_login():
    return render_template('gdg-article/account/login.html')

@app.route('/account/logout')
def account_logout():
    return redirect(url_for('home'))


@app.route('/helper')
def helper():
    return render_template("gdg-article/help-desk/gdg-ssu-help.html")



@app.route('/test')
def test():
    user = UserDB(user_id='youdskaj', user_pw='textpw1212')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/test12')
def test12():
    user = UserDB.query.all()
    # print(user)
    # print(user[0].user_id)

    return render_template("gdg-article/help-desk/temp_test.html", test_db=user)


@app.route('/tempform', methods=['GET', 'POST'])
def tempForm():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        print('forms ok')
    else:
        print('forms no')

    return render_template("gdg-article/help-desk/temp_form.html", form=form)

# @app.route('/temp12')
# def temp12():
#     return render_template("base/layout.html")
