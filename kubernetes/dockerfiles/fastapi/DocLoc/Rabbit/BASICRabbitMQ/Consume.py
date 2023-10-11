import pika

# Establece la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara una cola
channel.queue_declare(queue='mi_cola')

def callback(ch, method, properties, body):
    print(f" [x] Recibido '{body}'")

# Establece el callback para recibir mensajes
channel.basic_consume(queue='mi_cola',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Esperando mensajes. Para salir, presiona Ctrl+C')
channel.start_consuming()