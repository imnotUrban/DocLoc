from sqlalchemy import and_
from typing import List, Annotated
from config.db import conn
from datetime import datetime
from models.document import documents
from schemas.document import Document
from fastapi import APIRouter, Query

api = APIRouter()

@api.get("/all", response_model=List[Document])
def all():
   return conn.query(documents).all()

@api.get("/query", response_model=List[Document])
def filters(from_: str | None = None, to_: str | None = None, cat: str | None = None, page: int = 1):
   query = conn.query(documents)
   default_from =  "1970-01-01"
   default_to = datetime.now().strftime('%Y-%m-%d')
   page = 1 if page < 1 else page
   start_index = (page - 1) * 10
   end_index = page * 10

   if from_ and to_ and cat: # Si vienen los tres parametros en la query
      return query.filter(and_(documents.c.date >= from_, documents.c.date <= to_, documents.c.category == cat))[start_index:end_index]
   
   elif from_ and to_:
      return query.filter(and_(documents.c.date >= from_, documents.c.date <= to_))[start_index:end_index]

   elif from_ and cat:
      return query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to, documents.c.category == cat))[start_index:end_index]

   elif to_ and cat:
      return query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_, documents.c.category == cat))[start_index:end_index]

   elif from_:
      return query.filter(and_(documents.c.date >= from_, documents.c.date <= default_to))[start_index:end_index]

   elif to_:
      return query.filter(and_(documents.c.date >= default_from, documents.c.date <= to_))[start_index:end_index]

   elif cat: # Viene solo cat
      return query.filter(and_(documents.c.date >= default_from, documents.c.date <= default_to, documents.c.category == cat))[start_index:end_index]

   else:
      return query[start_index:end_index]


