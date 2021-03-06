from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, file_required
from wtforms import StringField, validators, PasswordField, TextAreaField
from .extensions.custom_validators import duplicate_check

__author__ = 'Genus'


class UserRegisterForm(Form):
    user_id = StringField(
            label=u'아이디',
            validators=[validators.length(min=6, max=20, message=u'아이디 형식을 지켜주세요.'),
                        validators.regexp(regex=r"^[a-z0-9]*$", message=u'아이디 형식을 지켜주세요'),
                        duplicate_check('user_table', 'user_id', message=u'아이디가 중복됩니다.')],
            description=u'아이디는 띄어쓰기 없이 영소문자/숫자만 가능합니다.'
    )
    password = PasswordField(
            label=u'비밀번호',
            validators=[validators.length(min=4, max=30, message=u'비밀번호의 형식을 지켜주세요')],
            description=u"비밀번호는 4~30의 모든 문자가 가능합니다"
    )
    confirm_password = PasswordField(
            label=u'비밀번호 확인',
            validators=[validators.equal_to('password')],
            description=u'보안을 위해 비밀번호 확인을 입력해주세요'
    )

class UserProfileForm(Form):
    name = StringField(
        label=u'이름',
        validators=[validators.data_required(message=u'이름을 입력하여주세요.')],
        description=u'이름을 입력해주세요'
    )
    desc = StringField(
        label=u'자기소개',
        validator=[validators.data_required(message=u'자기소개를 입력하여주세요.')],
        description=u'간략하게 소개해주세요'
    )
    picture = FileField(
        label=u'사진',
        validators=[file_required(message=u'사진을 첨부하여주세요.')],
        description=u'사진을 첨부해주세요.'
    )




class UserPortfolioForm(Form):
    title = StringField(
        label = u'프로젝트 이름',
        validators=[validators.data_required(message=u'프로젝트 이름을 입력해주세요'),
                    validators.length(min=1, max=30, message=u'프로젝트 이름은 최소 1자 최대 30자입니다.')],
        description=u'프로젝트 이름을 입력해주세요.'
    )
    title_desc = StringField(
        label=u'부연설명',
        validators=[validators.length(max=50,message=u'최대 50자까지 가능합니다.')],
        description=u'간략하게 설명해주세요.'
    )
    content = StringField(
        label=u'내용',
        validators=[validators.length(min=4, max=255, message=u'최소 4자 최대 255자만 가능합니다')],
        description=u'상세하게 설명해주세요~!'
    )
    pictures = FileField(
        label=u'이미지',
        description=u'이미지를 첨부해주세용'
    )



class UserLoginForm(Form):
    user_id = StringField(
            label=u'아이디',
            validators=[validators.data_required(message=u'아이디를 입력하여주세요.')]
    )
    password = PasswordField(
            label=u'비밀번호',
            validators=[validators.data_required(message=u'비밀번호를 입력하여주세요.')]
    )

class HelpDeskForm(Form):
    help_title = StringField(
        label=u'제목',
        validators = [validators.data_required(message=u'제목은 반드시 입력해주셔야 합니다.'),
                      validators.length(min=5,max=200,message=u'제목은 최소 5자 최대 200자까지만 가능합니다.')],
        description=u'제목'
    )
    help_content = TextAreaField(
        label=u'내용',
        validators=[validators.data_required(message=u'내용은 반드시 입력하여 주셔야 합니다.'),
                    validators.length(min=10,message=u'최소 10자 이상을 입력하여 주셔야합니다.')],
        description=u'내용'
    )
    author_name = StringField(
        label=u'이름',
        validators= [validators.data_required(message=u'이름을 입력하여주세요.')],
        description=u'이름을 입력하여주세요. 다른 사람들은 볼 수 없습니다.'
    )
    author_univ = StringField(
        label=u'소속 대학',
        validators=[validators.data_required(message=u'소속을 입력해 주세요.')],
        description=u'소속을 입력하여주세요'
    )
    author_major = StringField(
        label=u'전공',
        validators=[validators.data_required(message=u'전공을 입력하여주세요')],
        description=u'전공을 입력하여주세요'
    )
    author_tel= StringField(
        label=u'연락처',
        validators=[validators.data_required(message=u'연락처를 입력하여주세요')],
        description=u'연락처를 입력하여주세요. 컨택을 위해 필요합니다.'
    )
    password = PasswordField(
        label=u'비밀번호',
        validators=[validators.data_required(message=u'비밀번호를 입력하여주세요. 글 수정시 필요합니다')],
        description=u'비밀번호를 입력하여주세요. 글 수정시 필요합니다'
    )
