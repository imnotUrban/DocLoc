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

def setupRabbitmq():
    def callback(ch, method, properties, body):
        print(f" Recibido '{body}'")

    # Definir función de consumidor para el primer canal
    def consumeInputMessages():
        rabbitmqHost = 'localhost'
        rabbitmqPort = 5672

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
        channel = connection.channel()

        channel.queue_declare(queue='input')

        channel.basic_consume(queue='input',
                              on_message_callback=callback,
                              auto_ack=True)
        channel.start_consuming()

    # Definir función de consumidor para el segundo canal
    def consumeMiddleMessages():
        rabbitmqHost = 'localhost'
        rabbitmqPort = 5672

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
        channel = connection.channel()

        channel.queue_declare(queue='middle')

        channel.basic_consume(queue='middle',
                              on_message_callback=callback,
                              auto_ack=True)
        channel.start_consuming()

    # Crear hilos para ejecutar los consumidores en paralelo
    consumer_thread_channel1 = threading.Thread(target=consumeInputMessages)
    consumer_thread_channel2 = threading.Thread(target=consumeMiddleMessages)

    # Iniciar los hilos de los consumidores
    consumer_thread_channel1.start()
    consumer_thread_channel2.start()
