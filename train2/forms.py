from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, SelectField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange

# 회원가입 폼 생성
class UserCreateForm(FlaskForm):
  username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
  password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
  password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
  email = EmailField('이메일', validators=[DataRequired(), Email()])
  age = IntegerField('나이', validators=[DataRequired(), NumberRange(min=0, max=120, message="나이는 0에서 120 사이여야 합니다.")])
  sex = SelectField('성별',
        choices=[
            ('man', '남성'),
            ('woman', '여성'),
            ('other', '기타'),
        ],
        validators=[DataRequired()])
  job = SelectField(
    '직군',
    choices=[
        ('medical', '의료 및 보건'),
        ('public_admin', '공공 서비스 및 행정'),
        ('industry_tech', '산업 및 기술'),
        ('education', '교육 및 인재 양성'),
        ('environment', '환경 및 농림수산업'),
        ('finance', '금융 및 경영'),
        ('legal', '법률 및 사법'),
        ('it', 'IT 및 디지털 기술'),
        ('manufacturing', '노동 및 제조업'),
        ('logistics', '물류 및 교통'),
        ('culture', '문화 및 콘텐츠'),
        ('construction', '건설 및 도시 개발'),
        ('freelance', '자영업 및 프리랜서'),
        ('other', '기타'),
    ],
      validators=[DataRequired()]) 

  economy = BooleanField('경제')
  welfare = BooleanField('사회 및 복지')
  security = BooleanField('안보 및 외교')
  environment = BooleanField('환경 및 에너지')
  political_reform = BooleanField('행정 및 정치개혁')
  technology = BooleanField('기술 및 혁신')
  human_rights = BooleanField('인권 및 이민')
  defense = BooleanField('국방 및 군사')
  legislation = BooleanField('법률 및 사법')

# 로그인 폼 생성
class UserLoginForm(FlaskForm):
  username = StringField('닉네임', validators=[DataRequired(), Length(min=3, max=25)])
  password = PasswordField('비밀번호', validators=[DataRequired()])

# 정치성향검사기 폼 생성
class TestForm(FlaskForm):
    q1 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q2 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q3 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q4 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q5 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q6 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q7 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q8 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q9 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q10 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q11 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q12 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q13 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q14 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q15 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q16 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q17 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q18 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q19 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q20 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q21 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q22 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q23 = RadioField(
        choices=[
            ("0", "매우 동의"),
            ("0", "동의"),
            ("0", "중립"),
            ("0", "비동의"),
            ("0", "매우 비동의"),
        ],
        default="0"
    )
    q24 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q25 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q26 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q27 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q28 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q29 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q30 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q31 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q32 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q33 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q34 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q35 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q36 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q37 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q38 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q39 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q40 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q41 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q42 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q43 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q44 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q45 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q46 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q47 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q48 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q49 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q50 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q51 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q52 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q53 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q54 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q55 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q56 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q57 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q58 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )
    q59 = RadioField(
        choices=[
            ("2000", "매우 동의"),
            ("1000", "동의"),
            ("0", "중립"),
            ("1", "비동의"),
            ("2", "매우 비동의"),
        ],
        default="0"
    )
    q60 = RadioField(
        choices=[
            ("2", "매우 동의"),
            ("1", "동의"),
            ("0", "중립"),
            ("1000", "비동의"),
            ("2000", "매우 비동의"),
        ],
        default="0"
    )