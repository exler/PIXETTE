import secrets


class Config:
    """Base configuration"""

    SECRET_KEY = secrets.token_urlsafe(16)


class ProdConfig(Config):
    ENV = "production"
    DEBUG = False


class DevConfig(Config):
    ENV = "development"
    DEBUG = True