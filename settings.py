import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "connect_timeout": 15,
            "sslmode": "require",  # ← Ajout obligatoire pour Supabase
        },
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "connect_timeout": 15,
            "sslmode": "require",
        },
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "echo": True,  # ← Affiche les requêtes SQL en dev
    }


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "connect_timeout": 15,
            "sslmode": "require",
        },
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "pool_size": 5,  # ← Limite les connexions en prod
        "max_overflow": 10,
    }


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
