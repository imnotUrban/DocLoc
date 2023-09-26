import pika

# Establece la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara una cola
channel.queue_declare(queue='mi_cola')

# Envía un mensaje
message = 'Hola, RabbitMQ!'
channel.basic_publish(exchange='',
                      routing_key='mi_cola',
                      body=message)

print(f" [x] Enviado '{message}'")

# Cierra la conexión
connection.close()
