
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:1234@localhost/ip'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

