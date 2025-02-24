from crewai.tools import BaseTool
from pydantic import Field
import os
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Type

url: str = "https://bpqbutqtitrpidaghgme.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwcWJ1dHF0aXRycGlkYWdoZ21lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA0MDg4NDAsImV4cCI6MjA1NTk4NDg0MH0.QAUgaa-_h-aKbrn1O5cX4U3pJoETnZtt2KIzJKe7DJI"
supabase: Client = create_client(url, key)

class SupabaseInsertRowInputTool(BaseModel):
    table_name: str = Field(..., description="String containing the table name.")
    data: dict = Field(..., description="Dictionary containing the data to insert.")

class SupabaseInsertRowTool(BaseTool):
    name: str = "Supabase Insert Row Tool"
    description: str = "This tool is useful for inserting a row into the Supabase database, given the table name and the data to insert."
    
    args_schema: Type[BaseModel] = SupabaseInsertRowInputTool

    def _run(self, table_name: str, data: dict):
        try:
            result = supabase.table(table_name).insert(data).execute()
            return result
        except Exception as e:
            print(f"Error in SupabaseInsertRowTool: {str(e)}")
            raise e
