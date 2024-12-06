from train2 import db

# 사용자 정보 데이터베이스 생성

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  age = db.Column(db.Integer, nullable=False) 
  sex = db.Column(db.String(20), nullable=False) 
  job = db.Column(db.String(150), nullable=False)  
  
  economy = db.Column(db.Boolean, default=False)
  welfare = db.Column(db.Boolean, default=False)
  security = db.Column(db.Boolean, default=False)
  environment = db.Column(db.Boolean, default=False)
  political_reform = db.Column(db.Boolean, default=False)
  technology = db.Column(db.Boolean, default=False)
  human_rights = db.Column(db.Boolean, default=False)
  defense = db.Column(db.Boolean, default=False)
  legislation = db.Column(db.Boolean, default=False)

class Result(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  economy = db.Column(db.Boolean, nullable=True)
  welfare = db.Column(db.Boolean, nullable=True)
  security = db.Column(db.Boolean, nullable=True)
  environment = db.Column(db.Boolean, nullable=True)
  political_reform = db.Column(db.Boolean, nullable=True)
  technology = db.Column(db.Boolean, nullable=True)
  human_rights = db.Column(db.Boolean, nullable=True)
  defense = db.Column(db.Boolean, nullable=True)
  legislation = db.Column(db.Boolean, nullable=True)
  total = db.Column(db.Boolean, nullable=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=True)