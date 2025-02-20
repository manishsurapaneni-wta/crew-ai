from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://szlumttvfjcbxktpdrkf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6bHVtdHR2ZmpjYnhrdHBkcmtmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk5NDk5NzksImV4cCI6MjA1NTUyNTk3OX0.tBFIeCFQESejMBDcDEP0b5WOa-O8fq_RWSOQa3Hi2zk"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
