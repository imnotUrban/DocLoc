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
        raise HTTPException(status_code=406, detail="Debe enviar al menos un documento")

    try:
        doc =  document[0]
        result = doc.exists()
        if result is not None:
            return result
    
        GPTResult = queryEngine.query(doc.text)
        doc.updateSummary(GPTResult["data"]["summary"])
        doc.updateDocState(1) # Se obtuvo resumen y ubicación

        geoResult = geoloc.getCoordinates(GPTResult["data"])
        if geoResult['lat'] != " ":
            doc.updateDocLocLatLng(geoResult['location'], geoResult['lat'], geoResult['lng'])
            doc.updateDocState(2) # Se obtuvo lat y lng y se guarda en db
            doc.saveDocin()
            return doc.geolocalized()
        else:
            return {"msg": f"{geoResult['location']}, no es una ubicación válida"}
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación {str(e)}")
