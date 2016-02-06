from flask.ext.wtf import Form
from wtforms import StringField, validators, PasswordField

__author__ = 'Genus'


class UserRegisterForm(Form):
    user_id = StringField(
            label=u'아이디',
            validators=[validators.length(min=6, max=20, message=u'아이디 형식을 지켜주세요.'),
                        validators.regexp(regex=r"^[a-z0-9]*$", message=u'아이디 형식을 지켜주세요')],
            description=u'아이디는 띄어쓰기 없이 영소문자/숫자만 가능합니다.'
    )
    password = PasswordField(
            label=u'비밀번호',
            validators=[validators.Length(min=4, max=30, message=u'비밀번호의 형식을 지켜주세요')],
            description=u"비밀번호는 4~30의 모든 문자가 가능합니다"
    )
    confirm_password = PasswordField(
            label=u'비밀번호 확인',
            validators=[validators.data_required('필드를 입력하여주세요.')],
            description = u'보안을 위해 비밀번호 확인을 입력해주세요'
    )


    #
    # class JoinForm(Form):
    #     user_id = StringField(
    #         label=u'회원 ID',
    #         validators=[validators.data_required(u'회원 ID를 입력하시기 바랍니다.'),
    #                     validators.Length(min=6, max=20, message=u'ID는 6~20자 입니다.')],  # length: 6~15
    #         description={'placeholder': u'회원 ID를 입력하세요.'}
    #     )
    #     password = PasswordField(
    #         label=u'패스워드',
    #         validators=[validators.data_required(u'비밀번호를 입력하시기 바랍니다.'),
    #                     validators.Length(min=6, max=20, message=u'비밀번호는 6~15자가 필요합니다.'),
    #                     validators.EqualTo('confirm_password', message=u'비밀번호가 일치하지 않습니다.')],  # length: 6~15
    #         description={'placeholder': u'비밀번호를 입력하세요.'}
    #     )
    #     confirm_password = PasswordField(
    #         label=u'패스워드 확인',
    #         validators=[validators.data_required(u'비밀번호를 한번 더 입력하시길 바랍니다.')],
    #         description={'placeholder': u'비밀번호를 입력하세요.'}
    #     )
