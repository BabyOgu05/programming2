from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# 김하람

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')

CORS(app)

# ORM
db.init_app(app)
migrate.init_app(app, db)

# 블루프린트
from .views import main_views, auth_views, test_views
app.register_blueprint(main_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(test_views.bp)