from fastapi import APIRouter,  HTTPException  #Define subrutas o rutas por separado
from typing import List
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from schemas.document import Document

MAXDOCUMENTS = 1  #Número máximo de documentos que se pueden enviar por vez a la API

document = APIRouter()
queryEngine = GPTQueryEngine()
geoloc = Geocoding()

@document.post("/geolocalize")
async def create_documents(document: List[Document]):
    
    if(len(document) > MAXDOCUMENTS):
        raise HTTPException(status_code=406, detail="Se permite un máximo de 1 documento a procesar por petición")
    elif(len(document) == 0):
        raise HTTPException(status_code=406, detail="debe enviar al menos un documento")

    try:
        doc =  document[0]
        result = doc.is_title_exists()
        if result is not None:
            return result
        doc.saveDocin()
        GPTResult = queryEngine.query(doc.text)
        doc.updateSummary(GPTResult["data"][0]["summary"])
        doc.updateDocState(1)
        geoResult = geoloc.getCoordinates(GPTResult["data"][0])
        lat = geoResult[0]['lat']
        lng = geoResult[0]['lng'] 
        doc.updateDocLatLng(lat, lng)
        doc.updateDocState(2)
        return geoResult[0]
    except Exception as e:
        raise HTTPException(status_code=422, detail="Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación")
