import os

class BaseConfig(object):
    DEBUG = False
    
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = os.environ['ALPHA_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['ALPHA_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    
class TestingConfig(BaseConfig):
    DEBUG = True
    
    

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "production_database_uri"



    