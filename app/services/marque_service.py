from app.repositories.marque_repository import (
    get_all,
    get_random,
    increment_likes,
    increment_skips,
)


def get_stats():
    return [m.to_dict() for m in get_all()]


def get_next_marque():
    marque = get_random()
    if marque:
        return marque.nom  # ← on retire l'incrément de vues ici
    return "Inconnue"


def handle_click(nom: str, action: str):
    nom = nom.strip()

    if action == "like":
        increment_likes(nom)  # ← incrémente likes + vues
    elif action == "skip":
        increment_skips(nom)  # ← incrémente vues uniquement

        nouvelle_marque = get_next_marque()

        return {"marque": nouvelle_marque, "stats": get_stats()}
