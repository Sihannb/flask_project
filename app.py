from app import create_app
from app.repositories.marque_repository import init_db

app = create_app()

with app.app_context():
    init_db()