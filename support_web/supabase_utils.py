from supabase import create_client, Client
from django.conf import settings

url: str = settings.SUPABASE_URL
key: str = settings.SUPABASE_ANON_KEY
supabase: Client = create_client(url, key)

def fetch_data(table_name):
    response = supabase.table(table_name).select("*").execute()
    return response.data

def insert_data(table_name, data):
    response = supabase.table(table_name).insert(data).execute()
    return response.data