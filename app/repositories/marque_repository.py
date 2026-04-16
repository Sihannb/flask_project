from app.extensions import get_supabase
from app.models.marque import Marque

MARQUES_INITIALES = [
    "Toyota",
    "BMW",
    "Mercedes",
    "Audi",
    "Ford",
    "Tesla",
    "Honda",
    "Renault",
    "Peugeot",
    "Volkswagen",
]


def init_db():
    supabase = get_supabase()

    for nom in MARQUES_INITIALES:
        exists = (
            supabase.table("marques").select("id").eq("nom", nom).limit(1).execute()
        )

        if not exists.data:
            supabase.table("marques").insert(
                {"nom": nom, "vues": 0, "likes": 0}
            ).execute()


def get_all() -> list[Marque]:
    supabase = get_supabase()
    response = supabase.table("marques").select("*").order("likes", desc=True).execute()
    return [Marque.from_dict(m) for m in response.data]


def get_random() -> Marque:
    supabase = get_supabase()
    response = supabase.rpc("get_random_marque").execute()
    if response.data:
        return Marque.from_dict(response.data[0])
    return None


def increment_vues(nom: str):
    supabase = get_supabase()
    current = supabase.table("marques").select("vues").eq("nom", nom).execute()
    if not current.data:
        return
    vues = (current.data[0].get("vues") or 0) + 1
    supabase.table("marques").update({"vues": vues}).eq("nom", nom).execute()


def increment_likes(nom: str):
    supabase = get_supabase()
    current = supabase.table("marques").select("vues, likes").eq("nom", nom).execute()
    if not current.data:
        return
    vues = (current.data[0].get("vues") or 0) + 1
    likes = (current.data[0].get("likes") or 0) + 1
    supabase.table("marques").update({"vues": vues, "likes": likes}).eq(
        "nom", nom
    ).execute()


def increment_skips(nom: str):
    supabase = get_supabase()
    current = supabase.table("marques").select("vues").eq("nom", nom).execute()
    if not current.data:
        return
    vues = (current.data[0].get("vues") or 0) + 1
    supabase.table("marques").update({"vues": vues}).eq("nom", nom).execute()
