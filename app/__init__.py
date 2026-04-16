from flask import Flask
from settings import config
from app.extensions import init_supabase
from app.controllers.marque_controller import marque_bp


def create_app(config_name="default"):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config[config_name])

    init_supabase(app)

    # ✅ seulement les routes ici
    app.register_blueprint(marque_bp)

    return app