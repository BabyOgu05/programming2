from flask import Blueprint, url_for, render_template, flash, request, redirect, session, g
from werkzeug.security import generate_password_hash, check_password_hash

from train2 import db
from train2.forms import UserCreateForm, UserLoginForm
from train2.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

# 회원 가입 함수
@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
  form = UserCreateForm()
  if request.method == 'POST' and form.validate_on_submit(): 
    user = User.query.filter_by(username=form.username.data).first() # 폼에 유저가 입력한 이름 가져오기
    user_email = User.query.filter_by(email=form.email.data).first() # 폼에 유저가 입력한 이메일 가져오기
    if not user and not user_email: # 만약 유저가 데이터베이스에 존재하지 않는다면
      user = User(username=form.username.data, password=generate_password_hash(form.password1.data), email=form.email.data, sex=form.sex.data, job=form.job.data, age=form.age.data,
      economy=form.economy.data, welfare=form.welfare.data, security=form.security.data, environment=form.environment.data, political_reform=form.political_reform.data,
      technology=form.technology.data, human_rights=form.human_rights.data, defense=form.defense.data, legislation=form.legislation.data)
      db.session.add(user)
      db.session.commit() # 유저 정보 데이터베이스에 커밋
      return redirect(url_for('main.index'))
    elif user: # 만약에 유저가 데이터베이스에 이미 존재한다면
      flash('이미 존재하는 사용자입니다.') 
    else: # 만약에 이메일이 데이터베이스에 이미 존재한다면
      flash('이미 존재하는 이메일입니다.')
  return render_template('auth/signup.html', form=form)

# 로그인 함수
@bp.route('/login/', methods=['GET', 'POST'])
def login():
  form = UserLoginForm()
  if request.method == 'POST' and form.validate_on_submit():
    error = None
    user = User.query.filter_by(username=form.username.data).first() # 폼에 유저가 입력한 이름 가져오기
    if not user: # 만약 데이터베이스에 유저가 존재하지 않는다면
      error = '존재하지 않는 사용자입니다'
    elif not check_password_hash(user.password, form.password.data): # 만약 폼에 유저가 입력한 비밀번호가 일치하지 않는다면
      error = '비밀번호가 올바르지 않습니다'
    if error is None:
      session.clear()
      session['user_id'] = user.id # 세션에 유저 저장 (로그인)
      return redirect(url_for('main.index'))
    flash(error)
  return render_template('auth/login.html', form=form)

# 로그인 된 사용자를 확인하는 함수
@bp.before_app_request
def load_logged_user():
  user_id = session.get('user_id')
  if user_id is None:
    g.user = None
  else:
    g.user = User.query.get(user_id)

# 로그아웃 함수
@bp.route('/logout/')
def logout():
  session.clear() # 세션의 사용자를 지움
  return redirect(url_for('main.index'))