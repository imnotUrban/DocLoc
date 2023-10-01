from fastapi import APIRouter  #Define subrutas o rutas por separado
from typing import List
from schemas.document import Document
import pika
import json
import os
from dotenv import load_dotenv

document = APIRouter()

load_dotenv(dotenv_path="../.env")
rabbitmqHost = os.getenv("RABBIT_HOST")
rabbitmqPort = os.getenv("RABBIT_PORT")

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

# la tan esperada cola
channel.queue_declare(queue='input')
channel.queue_declare(queue='output')

@document.post("/addDocuments")
async def create_documents(document: List[Document]):
    try:
        for doc in document:
            doc.saveDocin()
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
            deserializedData = json.loads(body)
            salida.append(deserializedData)
            docCount = docCount + 1
        return salida
    except Exception:
        return {"message": "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}

@document.get("/healthz")
async def kbrns():
    return {"msg": "ok"}