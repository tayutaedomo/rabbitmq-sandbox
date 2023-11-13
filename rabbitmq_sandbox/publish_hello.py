import os
import pika

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    connection.close()
