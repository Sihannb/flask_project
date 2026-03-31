import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {"connect_timeout": 15},
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}