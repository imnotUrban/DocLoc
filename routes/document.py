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
    channel.basic_publish(exchange='', routing_key='output', body=json.dumps(processed_document))


@document.post("/addDocuments")
async def create_documents(document: List[Document]):
    queryEngine = GPTQueryEngine()
    geoloc = Geocoding()
    xd = []
    try:
        for doc in document:
            doc.saveDocin()
            xd.append(doc)
            # print(doc.id)
            
            doc.saveDocin()

            message = doc.json()

            # Envia por el canal input el doc
            channel.basic_publish(exchange='',
                      routing_key='input',
                      body=message)
            print("publicado en canal")

            ##TODO CHATGPT
            #GPTResult = queryEngine.query(doc.text)
            # for item in GPTResult['data']:
            #     print(item['location'])
            
            # Actualiza el estado del documento a 1 (Que ha sido procesado por CHATGPT)
            # doc.updateDocState(1)

            ##TODO GEOCODING
            # geoResult = geoloc.getCoordinates(GPTResult["data"])
            
            # Actualiza el estado del documento a 2 (Que ha sido procesado por la API de google)
            # doc.updateDocState(2)

            ##TODO DEVOLVER LOS DOCUMENTOS PROCESADOS
            # print(geoResult)
        return {"msg": "Ok"} #Se espera que, al integrar todos los ... de la api, devuelva un json con los documetntos procesados
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

