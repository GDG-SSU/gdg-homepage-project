__author__ = 'Genus'

from gdg_flask import db


# base Model
# All models is inherited BaseModel
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class UserDB(BaseModel):
    __tablename__ = "user_table"

    user_id = db.Column(db.String(30))
    user_pw = db.Column(db.String(255))
    # Permission Table
    #  0: admin, 1: gdg_member, 2: another man (Guest)
    permission = db.Column(db.SMALLINT(), default=2)
    # is_unregister user (registered: is_active=True, unregisterd: is_active=False)
    is_active = db.Column(db.Boolean(), default=True)
    last_login = db.Column(db.DateTime(), default=db.func.current_timestamp())

    def __str__(self):
        return "User <%s>" % self.user_id


class UserProfile(BaseModel):
    __tablename__ = "user_profile"
    name = db.Column(db.String(20))
    company = db.Column(db.String(50))
    title = db.Column(db.String(50))
    picture = db.Column(db.String(255))
    desc = db.Column(db.Text())

    user_num = db.Column(db.ForeignKey('user_table.id'))
    user = db.relationship('UserDB', backref=db.backref('profile', lazy='dynamic'))

    def __str__(self):
        return "Profile <%s : %s>" % (self.user, self.name)


class ProfileRibbon(BaseModel):
    __tablename__ = 'profile_ribbon'
    abbr = db.Column(db.String(50))
    title = db.Column(db.String(50))
    link = db.Column(db.String(255))
    profile_id = db.Column(db.ForeignKey('user_profile.id'))
    user_profile = db.relationship('UserProfile', backref=db.backref('ribbons'))

    def __str__(self):
        return "Profile Ribbon <%s : %s>" % (self.abbr, self.user_profile.name)


class ProfileSocial(BaseModel):
    __tablename__ = 'profile_social'
    name = db.Column(db.String(30))
    link = db.Column(db.String(255))
    profile_id = db.Column(db.ForeignKey('user_profile.id'))
    user_profile = db.relationship('UserProfile', backref=db.backref('socials'))

    def __str__(self):
        return "Profile Ribbon <%s : %s>" % (self.name, self.user_profile.name)


# Portfolio & User N:N
portfolio_user = db.Table('member_portfolio',
                          db.Column('portfolio_id', db.Integer, db.ForeignKey('portfolio.id')),
                          db.Column('user_id', db.Integer, db.ForeignKey('user_table.id'))
                          )


# Set relationship For SQLAlchemy ORM
class PortFolio(BaseModel):
    __tablename__ = 'portfolio'
    title = db.Column(db.String(30))
    title_desc = db.Column(db.String(50))
    content = db.Column(db.String(255))
    picture = db.Column(db.String(255))
    users = db.relationship('UserDB', secondary=portfolio_user,
                            backref=db.backref('portfolio', lazy='dynamic'))


class GdgHelpDesk(BaseModel):
    """
        gdg_help_desk service.
        A man needing help about IT Solutions post that board.
    """
    __tablename__ = "t_gdg_help_desk"
    help_title = db.Column(db.String(200))
    help_content = db.Column(db.Text())

    author_name = db.Column(db.String(20))
    author_univ = db.Column(db.String(30))
    author_major = db.Column(db.String(30))
    author_ip = db.Column(db.String(15))
    author_tel = db.Column(db.String(15))
    article_password = db.Column(db.String(255))
