import psycopg2
from flask import current_app, g
from app.models.marque import Marque

MARQUES_INITIALES = [
    "Toyota", "BMW", "Mercedes", "Audi", "Ford",
    "Tesla", "Honda", "Renault", "Peugeot", "Volkswagen",
]


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(
            current_app.config["DATABASE_URL"],
            connect_timeout=10
        )
        return g.db  # ← était à l'intérieur du if, jamais retourné si déjà connecté


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS marques (
        id SERIAL PRIMARY KEY,
        nom VARCHAR(100) UNIQUE NOT NULL,
        vues INT DEFAULT 0,
        likes INT DEFAULT 0
    );
    """)
    for m in MARQUES_INITIALES:
        cur.execute("""
        INSERT INTO marques (nom) VALUES (%s)
        ON CONFLICT (nom) DO NOTHING;
        """, (m,))
        conn.commit()
        cur.close()
        # ← pas de conn.close() ici, close_db() s'en charge en fin de requête


def get_all() -> list[Marque]:
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT nom, vues, likes FROM marques ORDER BY likes DESC")
    rows = cur.fetchall()
    cur.close()
    return [Marque(nom, vues, likes) for nom, vues, likes in rows]


def get_random() -> Marque:
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT nom, vues, likes FROM marques ORDER BY RANDOM() LIMIT 1")
    row = cur.fetchone()
    cur.close()
    return Marque(*row) if row else None


def increment_vues(nom: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE marques SET vues = vues + 1 WHERE nom = %s", (nom,))
    conn.commit()
    cur.close()


def increment_likes(nom: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE marques SET likes = likes + 1 WHERE nom = %s", (nom,))
    conn.commit()
    cur.close()