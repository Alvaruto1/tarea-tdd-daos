import os


class Config(object):
    """Parent configuration class."""
    FLASK_APP="run.py"
    SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    APP_SETTINGS="development"
    ENV = 'development'
    DEBUG = False
    CSRF_ENABLED = True
    


class DevelopmentConfig(Config):
    """Configurations for Development."""      
    DEBUG = True
    

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    ENV = 'test'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True    
    

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    


class ProductionConfig(Config):
    """Configurations for Production."""
    ENV = 'production'
    DEBUG = True
    TESTING = False
    


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
