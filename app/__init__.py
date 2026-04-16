from flask import Flask
from settings import config
from app.extensions import init_supabase
from app.controllers.marque_controller import marque_bp
from app.repositories.marque_repository import init_db


def create_app(config_name="default"):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config[config_name])

    init_supabase(app)

    with app.app_context():
        init_db()  # ✅ insère les données initiales

        # ✅ Enregistre les routes
        app.register_blueprint(marque_bp)

        return app