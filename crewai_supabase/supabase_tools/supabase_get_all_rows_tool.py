from crewai.tools import BaseTool
from pydantic import Field
import os
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Type
from dotenv import load_dotenv

load_dotenv()

url: str = "https://bpqbutqtitrpidaghgme.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwcWJ1dHF0aXRycGlkYWdoZ21lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA0MDg4NDAsImV4cCI6MjA1NTk4NDg0MH0.QAUgaa-_h-aKbrn1O5cX4U3pJoETnZtt2KIzJKe7DJI"
supabase: Client = create_client(url, key)

class SupabaseGetAllRowsInputTool(BaseModel):
    table_name: str = Field(..., description="String containing the table name.")
    
class SupabaseGetAllRowsOutputTool(BaseModel):
    result: str = Field(..., description="String containing the result.")
    count: int = Field(..., description="Integer containing the count of rows.")

class SupabaseGetAllRowsTool(BaseTool):
    name: str = "Supabase Get All Rows Tool"
    description: str = "This tool is useful for getting all rows from the Supabase database."
    
    args_schema: Type[BaseModel] = SupabaseGetAllRowsInputTool
    
    def _run(self, table_name: str) -> SupabaseGetAllRowsOutputTool:
        # Get all rows
        result = supabase.table(table_name).select("*").execute()
        
        # Get count using count() function
        result_count = supabase.table(table_name).select("*", count='exact').execute()
        
        # Convert to string representation for result and get count from metadata
        result_str = str(result.data)
        count = result_count.count

        return SupabaseGetAllRowsOutputTool(
            result=result_str,
            count=count
        )
