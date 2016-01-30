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
    __tablename__= "user_table"
    user_id = db.Column(db.String(30))
    user_pw = db.Column(db.String(255))
    permission = db.Column(db.SMALLINT(), default=1)



# class GdgHelpDesk(BaseModel):
#     # 유저로 저장할지 안정했다.
#     __tablename__ = "t_gdg_help_desk"
#     help_title = db.Column(db.String(200))
#     help_content = db.Column(db.Text())
#     author_address = db.Column(db.String(15))
