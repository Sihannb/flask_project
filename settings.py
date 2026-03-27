import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}