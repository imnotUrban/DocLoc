from sqlalchemy import and_
from typing import List
from config.db import conn
from datetime import datetime
from models.document import documents
from schemas.document import Document
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

api = APIRouter()

class QueryOut(BaseModel):
   doc: List[Document]
   count: int

def make_out(result, start_index, end_index):
   return {"doc": result[start_index:end_index], "count": result.count()}

@api.get("/query", response_model=QueryOut)
def filters(all: str = None, from_: str | None = None, to_: str | None = None, cat: str | None = None, page: int | None = 1):
   query = conn.query(documents)
   default_from =  "1970-01-01"
   default_to = datetime.now().strftime('%Y-%m-%d')
   page = 1 if page < 1 else page
   start_index = (page - 1) * 10
   end_index = page * 10
   
   try:

      if all == "all":
         return {"doc": query.all(), "count": query.count()}

      elif from_ and to_ and cat: # Si vienen los tres parametros en la query
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= to_, documents.c.category == cat))
         return make_out(result, start_index, end_index)
      
      elif from_ and to_:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= to_))[start_index:end_index]
         return make_out(result, start_index, end_index)

      elif from_ and cat:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to, documents.c.category == cat))[start_index:end_index]
         return make_out(result, start_index, end_index)

      elif to_ and cat:
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_, documents.c.category == cat))[start_index:end_index]
         return make_out(result, start_index, end_index)

      elif from_:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to))[start_index:end_index]
         return make_out(result, start_index, end_index)

      elif to_:
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_))[start_index:end_index]
         return make_out(result, start_index, end_index)

      elif cat: 
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= default_to, documents.c.category == cat))[start_index:end_index]
         return make_out(result, start_index, end_index)
         
      else:
         return {"doc": [], "count": 0}

   except Exception as e:
      raise HTTPException(status_code=400, detail= f"Bad Request {str(e)}")