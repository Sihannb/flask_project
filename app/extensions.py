from supabase import create_client, Client
import os

supabase: Client = None

def init_supabase(app):
    global supabase

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")

    # ✅ Vérification obligatoire
    if not url or not key:
        raise Exception("❌ SUPABASE_URL ou SUPABASE_ANON_KEY manquant")

    supabase = create_client(url, key)

    print(f"✅ Supabase connecté : {url}")

    return supabase


def get_supabase() -> Client:
    if supabase is None:
        raise Exception("❌ Supabase non initialisé")
    return supabase