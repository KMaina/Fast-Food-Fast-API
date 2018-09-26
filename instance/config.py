import os

class Config(object):
    """Parent configuration class."""
    # SECRET_KEY = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    CSRF_ENABLED = True

class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    CSRF_ENABLED = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}