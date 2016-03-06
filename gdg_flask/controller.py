import os

from flask import render_template, url_for, redirect, request, jsonify, session, flash, send_from_directory
from gdg_flask import app, db
from werkzeug.security import generate_password_hash, check_password_hash

# customization
from .models import UserDB, ProfileSocial, ProfileRibbon, PortFolio, UserProfile
from .forms import UserLoginForm, UserRegisterForm, HelpDeskForm, UserProfileForm


# router
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
    list = []
    for i in range(10):
        member = {}
        member['job'] = i
        member['count'] = str(i)
        list.append(member)

    return render_template('gdg-article/about/members.html', list=list)


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

@app.route('/account/register', methods=['GET', 'POST'])
def account_register():
    # session_check
    if session.get('user_id'):
        return redirect('home')
    form = UserRegisterForm()
    script_list = ["js/account/register.js"]
    if request.method == 'POST' and form.validate():
        user_id = form.user_id.data
        password = form.password.data
        user = UserDB(
                user_id=user_id,
                user_pw=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user_id
        session['permission'] = user.permission
        return redirect(url_for('home'))
    return render_template('gdg-article/account/register.html', form=form, script_list=script_list)


@app.route('/account/login', methods=['GET', 'POST'])
def account_login():
    # session_check
    if session.get('user_id'):
        return redirect('home')

    form = UserLoginForm()
    if request.method == 'POST' and form.validate():
        user_id = form.user_id.data
        password = form.password.data

        sql_query = "SELECT * from user_table WHERE user_id='%s' and is_active=True" % user_id
        sql_prx = db.engine.execute(sql_query)
        user = sql_prx.fetchone()
        sql_prx.close()
        if user is None:
            flash(u'아이디 혹은 비밀번호가 틀렸습니다.', 'danger')
        elif not check_password_hash(user.user_pw, password):
            flash(u'아이디 혹은 비밀번호가 틀렸습니다.', 'danger')
        else:
            session['user_id'] = user.user_id
            session['permission'] = user.permission
            # Update user_table.last_login
            db.engine.execute(
                    "UPDATE user_table SET last_login=%s WHERE user_id='%s' and is_active=True " % (
                        db.func.now(), user_id)
            ).close()
            return redirect(url_for('home'))
    return render_template('gdg-article/account/login.html', form=form)


@app.route('/account/logout')
def account_logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/account/profile/register')
def register_profile():
    if not session.get('user_id') and session.get('permission') == 1:
        return redirect(url_for('home'))

    form = UserProfileForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        desc = form.desc.data
        picture = form.picture.data

    return render_template('gdg-article/account/profile/profile_register.html', form=form)


# /*/check/* 는 항상 검사등 check를 위해서 사용
@app.route('/account/check/field')
def account_registerForm_check():
    form = UserRegisterForm()

    field_id = request.args.get('field_id')
    field_value = request.args.get('field_value')

    field_bind_id = request.args.get('field_bind_id')
    field_bind_value = request.args.get('field_bind_value')

    if field_bind_id and field_bind_value:
        form[field_bind_id].data = field_bind_value

    form[field_id].data = field_value

    result = form[field_id].validate(form)
    # 만족시 True
    # Boolean

    return jsonify(result=result)


@app.route('/helper', methods=['GET', 'POST'])
def helper_make():
    form = HelpDeskForm()
    return render_template("gdg-article/help-desk/make_helper.html", form=form)


@app.route('/helper/lists')
def helper_list():
    form = HelpDeskForm()
    return render_template("gdg-article/help-desk/gdg-ssu-help.html", form=form)


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
    form = UserRegisterForm()
    if request.method == 'POST' and form.validate():
        print('forms ok')
    else:
        print('forms no')

    return render_template("gdg-article/help-desk/temp_form.html", form=form)


@app.route('/media/<filename>')
def media(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/media/profile/<profilename>')
def get_profile(profilename):
    profile_path = app.config['UPLOAD_FOLDER'] + '/profile/'

    return send_from_directory(profile_path, profilename)



# yaml 파일 옮기려고 임시로..
# 참조용으로 내비뒀습니다
"""
@app.route('/profile/upload')
def yml_profile_upload():
    # 현재 앱에 sqlalcehmy 객체

    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fp = FileParser(directory + '/gdg_flask/media/speakers.yml').ymlReading()
    social_set = ['google-plus', 'facebook', 'linkedin', 'github']
    i = 0
    for profile in fp:
        i += 1
        p_name = profile.get('name')
        if UserProfile.query.filter_by(name=p_name).first():
            continue
        p_company = profile.get('company')
        p_title = profile.get('title')
        p_picture = profile.get('thumbnailUrl')
        p_bio = profile.get('bio')
        p_ribbons = profile.get('ribbon')
        p_socials = profile.get('social')

        profile = UserProfile(
                name=p_name,
                company=p_company,
                title=p_title,
                picture=p_picture,
                desc=p_bio
        )
        db.session.add(profile)
        print(str(i)+ "ing")

        if p_ribbons:
            l = 0
            for ribbon in p_ribbons:
                ribbon_title = ribbon.get('title')
                ribbon_abbr = ribbon.get('abbr')
                ribbon_link = ribbon.get('url')
                profile_ribbon = ProfileRibbon(
                        title=ribbon_title,
                        abbr=ribbon_abbr,
                        link=ribbon_link,
                        user_profile=profile
                )
                db.session.add(profile_ribbon)
                print(str(i) + "-r-" + str(l))
                l += 1

        if p_socials:
            l = 0
            for social in p_socials:
                social_name = social.get('name')
                social_link = social.get('link')
                profile_social = ProfileSocial(
                        name=social_name,
                        link=social_link,
                        user_profile=profile
                )
                if social_name not in social_set:
                    print('없는 이름입니다 . %s' % social_name)
                db.session.add(profile_social)
                print(str(i) + "-s-" + str(l))
                l += 1

        print(str(i) + "  finished")
        db.session.commit()

    return 'OK'
"""
