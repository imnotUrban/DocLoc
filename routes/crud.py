from sqlalchemy import and_  #Define subrutas o rutas por separado
from config.db import conn
from models.document import documents
from schemas.document import Document
from fastapi import APIRouter,  HTTPException  #Define subrutas o rutas por separado

api = APIRouter(prefix="/api",)

@api.get("/news/all/", response_model=list[Document])
def all():
   return conn.query(documents).all()

# Recibe un número de página -> retorna los n elementos de la página
@api.get("/news/page/", response_model=list[Document])
def page(page: int):
    if(page< 1):
       page =1
    start_index = (page - 1) * 10
    end_index = page * 10
    result = conn.query(documents)[start_index:end_index]
    return result

# DD-MM-AAAA
@api.get("/news/date/", response_model=list[Document])
def by_date(from_, to_):
   return conn.query(documents).filter(and_(documents.c.date >= from_, documents.c.date <= to_)).all()

@api.get("/news/category/", response_model=list[Document])
def by_category(category = str):
   return conn.query(documents).filter(documents.c.category == category).all()

# @api.get("/news/category/", response_model=list[Document])
# def get_by_both(from_: Date, to_: Date, category = str):
#     return conn.query(documents).filter(documents.c.date >= from_, documents.c.date <= to_).all() and db.query(documents).filter(documents.c.category == category).all()