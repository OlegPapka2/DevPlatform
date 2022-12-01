from utils.env_utils import get_env_var
import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_env_var('DB_URL')
    SECRET_KEY = os.urandom(32)
    UPLOAD_FOLDER = os.path.join('static', 'profile_pictures')


class ProductionConfig(Config):
    DEBUG = False
