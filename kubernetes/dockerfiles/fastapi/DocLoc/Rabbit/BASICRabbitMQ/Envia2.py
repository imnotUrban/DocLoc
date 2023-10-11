import json
import pika
from pydantic import BaseModel


rabbitmqHost = 'localhost'
rabbitmqPort = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

channel.queue_declare(queue='middle')



messagejson = [{'location': 'zona insular de la región de Valparaíso, Isla de Pascua', 'summary': 'Se espera lluvia en la noche del sábado y toda la jornada del domingo.'}, {'location': 'zona continental de la región de Valparaíso', 'summary': 'Se esperan precipitaciones para este viernes durante la mañana y la tarde.'}, {'location': 'región Metropolitana', 'summary': 'El fenómeno se presentaría en la tarde y en la noche del viernes.'}, {'location': "Higgins", 'summary': 'El fenómeno comenzaría en la mañana y terminaría en la noche del viernes.'}, {'location': 'región de Maule', 'summary': 'Se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio.'}, {'location': 'Ñuble', 'summary': 'Caerían chubascos desde la tarde del sábado hasta la madrugada del domingo.'}, {'location': 'Biobío', 'summary': 'El pronóstico apunta a la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado.'}, {'location': 'La Araucanía', 'summary': 'Las precipitaciones se harían presente en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente.'}, {'location': 'Los Ríos', 'summary': 'Se espera que el fenómeno se haga presente todo el viernes y el sábado.'}, {'location': 'Los Lagos', 'summary': 'Se espera que el fenómeno se haga presente todo el viernes y el sábado, y también se extendería en la noche del domingo.'}, {'location': 'región de Aysén', 'summary': 'Se espera que caiga agua-nieve en la madrugada del 2 de junio, y luego se registrarían nevadas hasta la mañana y chubascos el resto de la jornada del domingo.'}, {'location': 'región de Magallanes, Torres del Paine', 'summary': 'Caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de nieve en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche.'}, {'location': 'Punta Arenas', 'summary': 'Presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo.'}]

message = json.dumps(messagejson)

channel.basic_publish(exchange='',
                      routing_key='middle',
                      body=message)

print(f" [x] Enviado '{message}'")

# Cierra la conexión
connection.close()