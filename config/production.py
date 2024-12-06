from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'appdatabase.db'))
SQLALFHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x1f\xfe\r_\xe0g\x13#\x80\xc6\x9a\xc9V\xbb\xde\x9d'