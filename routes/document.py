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

# conexión RabbitMQ
rabbitmqHost = 'localhost'  # lo de abajo tambien
rabbitmqPort = 5672  # NOSE QUE PUERTO USAR asi que use el basico de rabbit xd

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

# la tan esperada cola
channel.queue_declare(queue='document_processed')


# Función para enviar un documento procesado a RabbitMQ
def send_processed_document(doc):
    processed_document = {
        "id": doc.id,
        "text": doc.text,
        # solo use estos campos para testear
    }
    channel.basic_publish(exchange='', routing_key='document_processed', body=json.dumps(processed_document))

# Ruta para procesar documentos y enviarlos a RabbitMQ
@document.post("/addDocuments")
async def create_documents(document: List[Document]):
    queryEngine = GPTQueryEngine()
    geoloc = Geocoding()
    try:
        for doc in document:
            doc.saveDocin()

            # Procesa el documento con GPT
            GPTResult = queryEngine.query(doc.text)
            doc.updateDocState(1)

            # Procesa el resultado de GPT para obtener coordenadas
            geoResult = geoloc.getCoordinates(GPTResult["data"])
            doc.updateDocState(2)

            # Envía el documento procesado a RabbitMQ
            send_processed_document(doc)

        return {"message": "Documentos procesados correctamente"}
    except Exception:
        return {"message": "Ha habido un error al ingresar el documento, intente seguir el formato indicado en la documentación"}

# consumidor testing de documentos
def process_document_message(ch, method, properties, body):
    try:
        # Procesa el mensaje recibido de RabbitMQ
        processed_document = json.loads(body)

        print("Documento procesado:", processed_document)
    except Exception as e:
        print("Error al procesar el mensaje de RabbitMQ:", e)

# CONSUMIDOR TESTING - no me funca los imports
channel.basic_consume(queue='document_processed', on_message_callback=process_document_message, auto_ack=True)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)









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

