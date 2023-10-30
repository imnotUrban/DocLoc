from sqlalchemy import and_  #Define subrutas o rutas por separado
from typing import List
from config.db import conn
from models.document import documents
from schemas.document import Document
from fastapi import APIRouter, HTTPException  #Define subrutas o rutas por separado

api = APIRouter(prefix="/api",)

@api.get("/all", response_model=List[Document])
def all():
   return conn.query(documents).all()

# Recibe un número de página -> retorna los n elementos de la página
@api.get("/page", response_model=List[Document])
def page(page: int):
   if page < 1:
      page = 1
   start_index = (page - 1) * 10
   end_index = page * 10
   result = conn.query(documents)[start_index:end_index]
   indexes_to_remove = []

   for i, doc in enumerate(result):
      if doc[5] in [1,2] or doc[8] == " " or doc[9] == " ": # Retonar solo las que tienen contenido
         indexes_to_remove.append(i)
         result += conn.query(documents)[end_index:end_index+1]
         end_index = end_index + 1

   for i in reversed(indexes_to_remove):
      result.pop(i)
   return result

# DD-MM-AAAA
@api.get("/date", response_model=List[Document])
def by_date(from_, to_):
   return conn.query(documents).filter(and_(documents.c.date >= from_, documents.c.date <= to_)).all()

@api.get("/category", response_model=List[Document])
def by_category(category = str):
   return conn.query(documents).filter(documents.c.category == category).all()

# @api.get("/news/category/", response_model=list[Document])
# def get_by_both(from_: Date, to_: Date, category = str):
#     return conn.query(documents).filter(documents.c.date >= from_, documents.c.date <= to_).all() and db.query(documents).filter(documents.c.category == category).all()