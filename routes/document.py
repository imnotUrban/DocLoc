from fastapi import APIRouter  #Define subrutas o rutas por separado
from typing import List
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from config.db import conn
from models.document import documents
from schemas.document import Document
from utils.jsonnify import transform_to_json
import pika
import json

document = APIRouter()

# conexión RabbitMQ input
rabbitmqHost = 'localhost'
rabbitmqPort = 5672
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

# la tan esperada cola
channel.queue_declare(queue='input')


# Función para enviar un documento procesado a RabbitMQ-- TODO
def send_processed_document(doc):
    processed_document = {
        "id": doc.id,
        "text": doc.text,
        # solo use estos campos para testear
    }
    channel.basic_publish(exchange='', routing_key='output', body=json.dumps(ss))

# Ruta para procesar documentos y enviarlos a RabbitMQ
@document.post("/addDocuments")
async def create_documents(document: List[Document]):
    queryEngine = GPTQueryEngine()
    geoloc = Geocoding()
    try:
        for doc in document:
            doc.saveDocin()

            # Envia por el canal input el doc
            channel.basic_publish(exchange='',
                      routing_key='input',
                      body=doc)
            
            # Procesa el documento con GPT
            #GPTResult = queryEngine.query(channel)
            doc.updateDocState(1)

            # Procesa el resultado de GPT para obtener coordenadas
            #geoResult = geoloc.getCoordinates(GPTResult["data"])
            #doc.updateDocState(2)

            # Envía el documento procesado a RabbitMQ
            #send_processed_document(doc]

        return {"message": "Documentos procesados correctamente"}
    except Exception:
        return {"message": "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}

#consume gpt

# #TODO: Aún no devuelve los documentos pq hay que transformalo a json a mano, pero no lo necesitamos en todo caso asi que se puede borrar esta ruta pq solo usamos una ruta jijijjiji
# @document.get("/documents")
# async def get_documents():
#     results =conn.execute(documents.select()).fetchall()
#     json_result = transform_to_json(results)
#     return json_result

