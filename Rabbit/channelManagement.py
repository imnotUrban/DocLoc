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
import threading

#rabbitmqPort = 5672 # puerto default rabbit
rabbitmqHost = 'localhost'
rabbitmqPort = 5672

queryEngine = GPTQueryEngine()
geoloc = Geocoding()

def setupRabbitmq():
    # Definir función de consumidor para el primer canal
    def consumeInputMessages():

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
        channel = connection.channel()

        channel.queue_declare(queue='input')

        def processInputChannel(ch, method, properties, body):
            doc = Document(**json.loads(body))

            GPTResult = queryEngine.query(doc.text)
            doc.updateDocState(1)

            channel.queue_declare(queue='middle')

            message = json.dumps(GPTResult["data"])

            doc.updateDocState(2)
            channel.basic_publish(exchange='',
                        routing_key='middle',
                        body=message)

        channel.basic_consume(queue='input',
                              on_message_callback=processInputChannel,
                              auto_ack=True)
        channel.start_consuming()

    # Definir función de consumidor para el segundo canal
    def consumeMiddleMessages():

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
        channel = connection.channel()

        channel.queue_declare(queue='middle')
        channel.queue_declare(queue='output')

        def processMiddleChannel(ch, method, properties, body):
            deserializedData = json.loads(body)
            geoResult = geoloc.getCoordinates(deserializedData) # Esto deberia volver a la ruta
            geoJson = json.dumps(geoResult)
            channel.basic_publish(exchange='',
                        routing_key='output',
                        body=geoJson)
            print("Esta todo en output queue...")

        channel.basic_consume(queue='middle',
                              on_message_callback=processMiddleChannel,
                              auto_ack=True)
        channel.start_consuming()

    # Crear hilos para ejecutar los consumidores en paralelo
    consumer_thread_channel1 = threading.Thread(target=consumeInputMessages)
    consumer_thread_channel2 = threading.Thread(target=consumeMiddleMessages)

    # Iniciar los hilos de los consumidores
    consumer_thread_channel1.start()
    consumer_thread_channel2.start()