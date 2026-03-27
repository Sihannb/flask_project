from app.repositories.marque_repository import (
    get_all,
    get_random,
    increment_vues,
    increment_likes,
)


def get_stats():
    return [m.to_dict() for m in get_all()]


def get_next_marque():
    marque = get_random()
    if marque:
        increment_vues(marque.nom)
        return marque.nom
    return "Inconnue"  # ✅ fallback réel

def handle_click(nom: str, action: str):
    nom = nom.strip() #nettoie les espaces invisibles
    
    if action == "like":
        increment_likes(nom)
    nouvelle_marque = get_next_marque()
    return {"marque": nouvelle_marque, "stats": get_stats()}  # ✅ toujours un dict valide