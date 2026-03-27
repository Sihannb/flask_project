from flask import Flask
from settings import config        # ← importe le dictionnaire
from app.repositories.marque_repository import init_db
from app.controllers.marque_controller import marque_bp
from app.repositories.marque_repository import close_db

def create_app(config_name="default"):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config[config_name]) 
    
    app.teardown_appcontext(close_db)  # ← ferme la connexion après chaque requête HTTP

    with app.app_context():
        init_db()

        app.register_blueprint(marque_bp)

    return app