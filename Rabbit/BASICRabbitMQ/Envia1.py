import pika

rabbitmqHost = 'localhost'
rabbitmqPort = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmqHost, port=rabbitmqPort))
channel = connection.channel()

channel.queue_declare(queue='input')


# Envía un mensaje
message = 'Hola, RabbitMQ1!'
channel.basic_publish(exchange='',
                      routing_key='input',
                      body=message)

print(f" [x] Enviado '{message}'")

# Cierra la conexión
connection.close()
