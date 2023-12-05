from typing import List
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import and_
from config.db import conn
from models.document import documents
from schemas.document import Document

def make_out(result, start_index, end_index):
   return {"doc": result[start_index:end_index], "count": result.count()}

def query_documents(all: str = None, from_: str | None = None, to_: str | None = None, cat: str | None = None, page: int | None = 1):
   default_from = "1970-01-01"
   default_to = datetime.now().strftime('%Y-%m-%d')
   page = 1 if page < 1 else page
   start_index = (page - 1) * 10
   end_index = page * 10
   
   try:
      query = conn.query(documents)

      if all == "all":
         return {"doc": query.all(), "count": query.count()}

      elif from_ and to_ and cat and page:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= to_, documents.c.category == cat))
         conn.commit()
         return make_out(result, start_index, end_index)
      
      elif from_ and to_ and page:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= to_))
         conn.commit()
         return make_out(result, start_index, end_index)

      elif from_ and cat and page:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to, documents.c.category == cat))
         conn.commit()
         return make_out(result, start_index, end_index)

      elif to_ and cat and page:
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_, documents.c.category == cat))
         conn.commit()
         return make_out(result, start_index, end_index)

      elif from_ and page:
         result = query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to))
         conn.commit()
         return make_out(result, start_index, end_index)

      elif to_ and page:
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_))
         conn.commit()
         return make_out(result, start_index, end_index)

      elif cat and page:
         result = query.filter(and_(documents.c.date >= default_from, documents.c.date <= default_to, documents.c.category == cat))
         conn.commit()
         return make_out(result, start_index, end_index)
         
      elif page:
         return {"doc": query[start_index:end_index], "count": query.count()}

   except Exception as e:
      conn.rollback()
      raise HTTPException(status_code=400, detail= f"Bad Request {str(e)}")
   finally:
      conn.close()