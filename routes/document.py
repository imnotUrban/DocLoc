from fastapi import APIRouter  #Define subrutas o rutas por separado

from config.db import conn

from models.document import documents

from schemas.document import Document

document = APIRouter()

@document.get("/documents")
def get_documents():
    results =conn.execute(documents.select()).fetchall()
    return results


@document.post("/addDocuments")
def create_documents(document: Document):
    newDocument = {"title" : document.title, "text": document.text, "date": document.date, "url":document.url, "state": 0}
    result = conn.execute(documents.insert().values(newDocument))
    conn.commit()
    print(result)
    
    return "ola"