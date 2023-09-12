from fastapi import APIRouter  #Define subrutas o rutas por separado

from typing import List

from gpt.GPTQueryEngine import GPTQueryEngine

from config.db import conn

from models.document import documents

from schemas.document import Document

from utils.jsonnify import transform_to_json

document = APIRouter()


@document.post("/addDocuments")
async def create_documents(document: List[Document]):
    queryEngine = GPTQueryEngine()
    xd = []
    try:
        for doc in document:
            doc.saveDocin()
            xd.append(doc)
            print(doc.id)
            
            ##TODO CHATGPT
            GPTResult = queryEngine.query(doc.text);
            for item in GPTResult['data']:
                print(item['location'])
            ##TODO GEOCODING
            
            ##TODO DEVOLVER LOS DOCUMENTOS PROCESADOS
            
        return {"message" : "Documentos procesados correctamente"} #Se espera que, al integrar todos los ... de la api, devuelva un json con los documetntos procesados
    except Exception:
        return {"message" : "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}
        



# @document.post("/addDocuments")
# async def create_documents(document: Document):
#     # newDocument = {"title" : document.title, "text": document.text, "date": document.date, "url":document.url, "state": 0}
#     # result = conn.execute(documents.insert().values(newDocument))
#     # conn.commit()
#     # print( result.inserted_primary_key[0]) #id del ultimo insertado
#     document.saveDocin()
#     print(document.id)
#     return "ok"



# #TODO: Aún no devuelve los documentos pq hay que transformalo a json a mano, pero no lo necesitamos en todo caso asi que se puede borrar esta ruta pq solo usamos una ruta jijijjiji
# @document.get("/documents")
# async def get_documents():
#     results =conn.execute(documents.select()).fetchall()
#     json_result = transform_to_json(results)
#     return json_result

