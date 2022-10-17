from utils.env_utils import get_env_var


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_env_var('DB_URL')


class ProductionConfig(Config):
    DEBUG = False
