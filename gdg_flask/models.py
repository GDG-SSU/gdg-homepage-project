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
    is_active = db.Column(db.Boolean(),default=True)
    last_login = db.Column(db.DateTime(), default=db.func.current_timestamp())



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
