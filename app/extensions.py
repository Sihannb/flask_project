from supabase import create_client, Client
import os

supabase: Client = None

def init_supabase(app):
    global supabase
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_ANON_KEY")
    )
    print(f"✅ Supabase connecté : {os.getenv('SUPABASE_URL')}")
    return supabase

def get_supabase() -> Client:
    return supabase