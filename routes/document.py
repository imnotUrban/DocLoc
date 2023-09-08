from fastapi import APIRouter  #Define subrutas o rutas por separado

from config.db import conn

from models.document import documents

from schemas.document import Document

document = APIRouter()

#TODO: Aún no devuelve los documentos pq hay que transformalo a json a mano, pero no lo necesitamos en todo caso asi que se puede borrar esta ruta pq solo usamos una ruta jijijjiji
@document.get("/documents")
def get_documents():
    results =conn.execute(documents.select()).fetchall()
    print(results)
    return "results_dict"


@document.post("/addDocuments")
def create_documents(document: Document):
    newDocument = {"title" : document.title, "text": document.text, "date": document.date, "url":document.url, "state": 0}
    result = conn.execute(documents.insert().values(newDocument))
    conn.commit()
    print(result)
    
    return result