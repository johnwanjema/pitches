import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:1234@localhost/ip'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

