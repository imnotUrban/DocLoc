import json
import pika
from pydantic import BaseModel



class Document(BaseModel):
    id: int | None = None
    title: str
    text: str
    date: str
    url: str
    state: int | None = None 
    result: str | None = None
    lat: str | None = None 
    long: str | None = None


rabbitmqHost = 'localhost'
rabbitmqPort = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

channel.queue_declare(queue='input')

documento = Document(
    id=0,
    title="Pronóstico de lluvia para el fin de semana: Revisa las zonas en las que se esperan precipitaciones",
    text="De acuerdo al reporte de la Dirección Meteorológica de Chile, ...",
    date="May 31, 2023 @ 20:00:00.000",
    url="https://www.meganoticias.cl/nacional/415732-lluvia-fin-de-semana-santiago-regiones-pronostico-del-tiempo-25-05-2023.html"
)

message = documento.json()


channel.basic_publish(exchange='',
                      routing_key='input',
                      body=message)

print(f" [x] Enviado '{message}'")

# Cierra la conexión
connection.close()