import os

class Config:
    DEBUG = False
    SECRET = os.getenv('SECRET')
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    DEBUG= True

class ProductionConfig(Config):
    DEBUG= False
    TESTING = False

app_config = {    

    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}