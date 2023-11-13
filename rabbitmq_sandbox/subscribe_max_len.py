import os
import datetime
import pika

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def callback(ch, method, properties, body):
    try:
        message = body.decode()

        print(f"{datetime.datetime.now()}, Received {message}")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error: {e}")


def subscribe(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    args = {
        "x-message-ttl" : 5 * 60 * 1000,
        "x-max-length": 2,
        "x-overflow": "reject-publish", # or "drop-head"
    }
    channel.queue_declare(queue=queue_name, arguments=args)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

    print('Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == "__main__":
    subscribe("max_len")
