from fastapi import APIRouter,  HTTPException  #Define subrutas o rutas por separado
from typing import List
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from schemas.document import Document

MAXDOCUMENTS = 1  #Número máximo de documentos que se pueden enviar por vez a la API

<<<<<<< HEAD
# la tan esperada cola
channel.queue_declare(queue='input')
channel.queue_declare(queue='middle')
channel.queue_declare(queue='output')
=======
document = APIRouter()
queryEngine = GPTQueryEngine()
geoloc = Geocoding()
>>>>>>> 0529dd781dccdea044d26fd6ac94626b4c5e5a03

@document.post("/geolocalize")
async def create_documents(document: List[Document]):
<<<<<<< HEAD
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
    channel = connection.channel()

    # la tan esperada cola
    channel.queue_declare(queue='input')
    channel.queue_declare(queue='middle')
    channel.queue_declare(queue='output')
=======
    
    if(len(document) > MAXDOCUMENTS):
        raise HTTPException(status_code=406, detail="Se permite un máximo de 1 documento a procesar por petición")
    elif(len(document) == 0):
        raise HTTPException(status_code=406, detail="debe enviar al menos un documento")

>>>>>>> 0529dd781dccdea044d26fd6ac94626b4c5e5a03
    try:
        
        for doc in document:
            doc.saveDocin()
<<<<<<< HEAD
            message = doc.json()

            # Envia por el canal input el doc
            channel.basic_publish(exchange='',
                      routing_key='input',
                      body=message)
            print("publicado en canal")

        docLen = len(document)
        salida = []
        docCount = 0
        while(docCount != docLen):
            _, _, body = channel.basic_get(queue='output')
            if body == None:
                robate_el_cielo = True
            else:
                deserializedData = json.loads(body)
                salida.append(deserializedData)
                docCount = docCount + 1
        connection.close()
        return salida


    except Exception:
        connection.close()
        return {"message": "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}
=======

            GPTResult = queryEngine.query(doc.text)
            doc.updateDocState(1)
>>>>>>> 0529dd781dccdea044d26fd6ac94626b4c5e5a03

            geoResult = geoloc.getCoordinates(GPTResult["data"])
            doc.updateDocState(2)

        return geoResult
    except Exception as e:
        raise HTTPException(status_code=422, detail="Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación")
