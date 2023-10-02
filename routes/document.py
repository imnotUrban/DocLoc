from fastapi import APIRouter  #Define subrutas o rutas por separado
from typing import List
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from config.db import conn
from models.document import documents
from schemas.document import Document
from utils.jsonnify import transform_to_json

document = APIRouter()
queryEngine = GPTQueryEngine()
geoloc = Geocoding()

@document.post("/geolocalize")
async def create_documents(document: List[Document]):
    try:
        for doc in document:
            doc.saveDocin()

            GPTResult = queryEngine.query(doc.text)
            doc.updateDocState(1)

            geoResult = geoloc.getCoordinates(GPTResult["data"])
            doc.updateDocState(2)

        return geoResult
    except Exception:
        return {"message" : "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}
