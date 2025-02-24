from crewai.tools import BaseTool
from pydantic import Field
import os
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Type

url: str = "https://bpqbutqtitrpidaghgme.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwcWJ1dHF0aXRycGlkYWdoZ21lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA0MDg4NDAsImV4cCI6MjA1NTk4NDg0MH0.QAUgaa-_h-aKbrn1O5cX4U3pJoETnZtt2KIzJKe7DJI"
supabase: Client = create_client(url, key)

class SupabaseDeleteRowInputTool(BaseModel):
    table_name: str = Field(..., description="String containing the table name.")
    column_name: str = Field(..., description="String containing the column name.")
    value: str = Field(..., description="String containing the value.")

class SupabaseDeleteRowTool(BaseTool):
    name: str = "Supabase Delete Row Tool"
    description: str = "This tool is useful for deleting a row from the Supabase database."
    
    args_schema: Type[BaseModel] = SupabaseDeleteRowInputTool

    def _run(self, table_name: str, column_name: str, value: str) -> str:
        result = supabase.table(table_name).delete().eq(column_name, value).execute()
        return result
