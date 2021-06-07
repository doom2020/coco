from re import DEBUG


class Config(object):
    pass
"""
通用配置(flask内置配置)
"""

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'dev'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = 'pro'

class TestingConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'test'