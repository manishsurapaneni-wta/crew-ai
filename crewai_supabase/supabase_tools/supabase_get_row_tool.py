from crewai.tools import BaseTool
import os
from supabase import create_client, Client

url: str = "https://bpqbutqtitrpidaghgme.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwcWJ1dHF0aXRycGlkYWdoZ21lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA0MDg4NDAsImV4cCI6MjA1NTk4NDg0MH0.QAUgaa-_h-aKbrn1O5cX4U3pJoETnZtt2KIzJKe7DJI"
supabase: Client = create_client(url, key)

class SupabaseGetRowTool(BaseTool):
    name: str = "Supabase Get Row Tool"
    description: str = "This tool is useful for getting a row from the Supabase database."

    def _run(self, table_name: str, column_name: str, value: str) -> str:
        result = supabase.table(table_name).select("*").eq(column_name, value).execute()
        return result
