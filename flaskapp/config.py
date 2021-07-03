"""
通用配置(flask内置配置)
"""


class Config(object):
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/main'
    SQLALCHEMY_BINDS = {
        'users': 'mysql://root:123456@127.0.0.1/users'
    }
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = 'pro'


class TestingConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'test'
