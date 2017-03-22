class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

    # Enable protection against Cross-site Request Forgery (CSRF)
    CSRF_ENABLED = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

    # Enable protection against Cross-site Request Forgery (CSRF)
    CSRF_ENABLED = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}